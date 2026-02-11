import warnings
import pytest
from sqlalchemy.exc import SAWarning

# Substrings from the warnings on build in Amanuensis logs (PEDS:1344)
OVERLAP_WARNING_SNIPPETS = [
    "relationship 'Project.associated_users_roles'",
    "relationship 'Project.search_in_project'",
    "relationship 'Request.request_has_state'",
    "relationship 'Statistician.projects'",
    "relationship 'AssociatedUser.projects'",
]


def test_no_sqlalchemy_overlap_warnings_on_import():
    # Capture warnings during import + mapper configuration
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always", SAWarning)

        # Importing these should trigger mapper configuration / inspection
        import userportaldatamodel.project  # noqa: F401
        import userportaldatamodel.search  # noqa: F401
        import userportaldatamodel.state  # noqa: F401
        import userportaldatamodel.statistician  # noqa: F401
        import userportaldatamodel.associated_user  # noqa: F401

    sa_warnings = [w for w in caught if issubclass(w.category, SAWarning)]
    overlap_hits = [
        w for w in sa_warnings
        if any(snippet in str(w.message) for snippet in OVERLAP_WARNING_SNIPPETS)
    ]

    assert overlap_hits == [], (
        "Expected no overlap-related SAWarnings, but got:\n"
        + "\n---\n".join(str(w.message) for w in overlap_hits)
    )
