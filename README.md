### Quick Start

Sample App Directory Hierarchy
```
my_app/
├── configs/
│   ├── app_config1.cfg
│   └── app_config2.cfg
└──  setting/
    ├── __init__.py
    └── setting.py
```

app_config1.cfg
```
[GENERAL]
is_production: true
application_name: application_name
application_description: application_description
application_version: application_version


[DATABASE]
host: host
port: 995
database: database
username: username
password: password
```


setting.py
```python
from os import sep
from configloader.utils import base_dir_path_finder, schema, add_dir_to_env
from configloader.loader import ConfigLoader

BASE_DIR_PATH = base_dir_path_finder(
    file_path=__file__,
    number_of_going_up=2
)

BASE_DIR_STR = str(BASE_DIR_PATH)

add_dir_to_env(path_=BASE_DIR_STR)

config_loader = ConfigLoader(
    configs_dir=BASE_DIR_STR + sep + "configs",
    active_section_schemas={
        "GENERAL": schema.General,
        "DATABASE": schema.Database,
    },

    raised_on_duplicate_sections=False,
    raised_on_unused_sections=False,
    raised_on_missed_sections=False,

    convert_to_orm_mode=True,
)

CONFIG = config_loader.perform()

print(CONFIG)
```

schema.py
```python
from pydantic import BaseModel

class General(BaseModel):
    is_production: bool
    application_name: str
    application_description: str
    application_version: str

    
class Database(BaseModel):
    host: str
    port: int
    database: str
    username: str
    password: str
```