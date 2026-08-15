from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.code_statistics import fortran_directive_comment


def test_fortran_directive_comment_detects_dec_and_dir_free_form():
    assert fortran_directive_comment("!DEC$ ATTRIBUTES DLLEXPORT :: FOO", free_form=True) == "dec$"
    assert fortran_directive_comment("!DIR$ IVDEP", free_form=True) == "dir$"


def test_fortran_directive_comment_detects_dec_and_dir_fixed_form():
    assert fortran_directive_comment("CDEC$ ATTRIBUTES DLLEXPORT :: FOO", free_form=False) == "dec$"
    assert fortran_directive_comment("*DIR$ IVDEP", free_form=False) == "dir$"


def test_fortran_directive_comment_ignores_plain_comments():
    assert fortran_directive_comment("! just a comment", free_form=True) is None
    assert fortran_directive_comment("C  a note about the algorithm", free_form=False) is None
