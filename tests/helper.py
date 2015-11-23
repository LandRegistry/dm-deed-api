class DeedModelMock:
    token = "ABC1234"
    deed = {"title_number": "DN100"}


class DeedHelper:
    _json_doc = {
        "title_number": "DN100",
        "borrowers": [
        {
            "forename": "lisa",
            "middle_name": "ann",
            "surname": "bloggette",
            "gender": "M",
            "address": "test address with postcode, PL14 3JR",
            "dob": "23/01/1986",
            "phone_number": "07502154062"
        },
        {
            "forename": "frank",
            "middle_name": "ann",
            "surname": "bloggette",
            "gender": "M",
            "address": "Test Address With Postcode, PL14 3JR",
            "dob": "23/01/1986",
            "phone_number": "07502154062"
        }
        ]
    }

    _invalid_title = {
        "title_number": "BBBB12313212BB",
        "borrowers": [
            {
                "forename": "fred",
                "middle_name": "joe",
                "surname": "bloggs"
            },
            {
                "forename": "lisa",
                "surname": "bloggette"
            }
        ]
    }
