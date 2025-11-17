import openminds.v4 as om


def test_invalid_type():
    # invalid: type
    mouse = om.controlled_terms.Species.mus_musculus
    dsv = om.core.DatasetVersion(accessibility=mouse)
    assert dsv.validate(ignore=["required"]) == {
        "type": ["accessibility: Expected ProductAccessibility, value contains Species"]
    }

    # valid
    dsv = om.core.DatasetVersion(study_targets=[mouse])
    assert dsv.validate(ignore=["required"]) == {}

    # invalid: doubly-nested list
    dsv = om.core.DatasetVersion(study_targets=[[mouse]])
    assert "value contains list" in dsv.validate(ignore=["required"])["type"][0]


def test_required():
    p = om.core.Person()
    assert p.validate() == {
        "required": [
            "given_name is required, but was not provided",
        ]
    }
