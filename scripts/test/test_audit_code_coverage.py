from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.audit_code import (
    CATEGORIES,
    build_category_rows,
    collect_unique_warnings,
    summarize_coverage,
    warning_counts,
)


def test_build_category_rows_includes_total_warning_count():
    results = [
        {
            "compiler": "gcc",
            "precision": "single",
            "counts": {
                "warnings": 10,
                "errors": 0,
                "obsolescent": 2,
                "implicit_interface": 3,
                "conversion": 1,
                "real_comparison": 2,
                "unused": 2,
                "tabs": 0,
                "c_sign_conversion": 0,
                "c_float_conversion": 0,
            },
        },
        {
            "compiler": "gcc",
            "precision": "double",
            "counts": {
                "warnings": 12,
                "errors": 1,
                "obsolescent": 3,
                "implicit_interface": 4,
                "conversion": 1,
                "real_comparison": 2,
                "unused": 2,
                "tabs": 0,
                "c_sign_conversion": 0,
                "c_float_conversion": 0,
            },
        },
    ]

    rows = build_category_rows(results, {"gcc"})

    assert rows == [
        ("gcc", "single", 10, 2, 3, 1, 2, 2, 0, 0, 0),
        ("gcc", "double", 12, 3, 4, 1, 2, 2, 0, 0, 0),
    ]


def test_build_category_rows_honors_selected_precisions():
    results = [
        {
            "compiler": "gcc",
            "precision": "single",
            "counts": {"warnings": 1, **{key: 0 for key, _, _ in CATEGORIES}},
        },
        {
            "compiler": "gcc",
            "precision": "double",
            "counts": {"warnings": 2, **{key: 0 for key, _, _ in CATEGORIES}},
        },
    ]

    assert build_category_rows(results, {"gcc"}, ("single",)) == [
        ("gcc", "single", 1, 0, 0, 0, 0, 0, 0, 0, 0),
    ]


def test_summarize_coverage_handles_gcovr_summary():
    summary = {
        "line_total": 100,
        "line_covered": 80,
        "line_percent": 80.0,
        "branch_total": 40,
        "branch_covered": 10,
        "branch_percent": 25.0,
        "function_total": 20,
        "function_covered": 14,
        "function_percent": 70.0,
    }

    assert summarize_coverage(summary) == {
        "line_covered": 80,
        "line_total": 100,
        "line_percent": 80.0,
        "branch_covered": 10,
        "branch_total": 40,
        "branch_percent": 25.0,
        "function_covered": 14,
        "function_total": 20,
        "function_percent": 70.0,
    }


def test_collect_unique_warnings_includes_independent_config_tags(tmp_path):
    log_file = tmp_path / "warning.log"
    log_file.write_text(
        "src/example.f:1:1:\n\n"
        "      CALL EXAMPLE\n"
        "      1\n"
        "Warning: Procedure 'example' called with an implicit interface at (1)\n",
        encoding="utf-8",
    )
    results = [
        {"compiler": "gcc", "build_type": "debug", "precision": "single", "log_file": log_file},
        {"compiler": "gcc", "build_type": "release", "precision": "single", "log_file": log_file},
    ]

    warnings = collect_unique_warnings(results)

    assert warnings[0]["tags"] == {
        "compiler:gcc",
        "build-type:debug",
        "build-type:release",
        "precision:single",
    }


def test_warning_counts_parses_intel_fortran_diagnostics(tmp_path):
    log_file = tmp_path / "intel.log"
    log_file.write_text(
        "../../src/utl7.f(1650): warning #6717: This name has not been given an explicit type.   [J]\n"
        "      ICRL= (K-1)*NROW*NCOL + (I-1)*NCOL + J\n"
        "-------------------------------------------^\n"
        "../../src/utl7.f(1670): warning #7346: The CHARACTER* form of a CHARACTER declaration is an "
        "obsolescent feature in Fortran 2018.\n"
        "      CHARACTER*(*) TEXT1,TEXT2\n"
        "-----------------^\n",
        encoding="utf-8",
    )

    counts = warning_counts(log_file)

    assert counts["warnings"] == 2
    assert counts["obsolescent"] == 1
    assert counts["implicit_interface"] == 1


def test_warning_counts_parses_back_to_back_c_diagnostics(tmp_path):
    log_file = tmp_path / "c_warnings.log"
    log_file.write_text(
        "../../src/ccfd.c:59:32: warning: implicit conversion changes signedness: "
        "'int' to 'unsigned long' [-Wsign-conversion]\n"
        "   59 |   CCFD_ptr->DD=(double*)calloc(neq,sizeof(double));\n"
        "      |                         ~~~~~~ ^~~\n"
        "../../src/ccfd.c:62:11: warning: implicit conversion changes signedness: "
        "'unsigned long' to 'int' [-Wsign-conversion]\n"
        "   62 |   size=neq*sizeof(double);\n"
        "      |       ~~~~^~~~~~~~~~~~~~~\n",
        encoding="utf-8",
    )

    counts = warning_counts(log_file)

    assert counts["warnings"] == 2