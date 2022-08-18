from email.policy import default


projects = [
   "test"
]

options = [
    {
        "option": "checkout",
        "params": [
            {
                "name": "",
                "value": "master"
            }
        ]
    },
    {
        "option": "merge",
        "params": [
            {
                "name":"",
                "value":"test"
            }
        ]
    }
]

work_path = "D:\\workspace\\zzh\\my-script\\git-script\\batch-operational"


default_options = [
    {
        "option": "checkout",
        "params": [
            {
                "name":"",
                "value":"prod"
            }
        ]
    },
    {
        "option": "pull",
        "params": [
            {
                "name":"",
                "value":""
            }
        ]
    },
    {
        "option": "push",
        "params": [
            {
                "name":"",
                "value":""
            }
        ]
    },
    {
        "option": "merge",
        "params": [
            {
                "name":"",
                "value":"test"
            }
        ]
    }
]