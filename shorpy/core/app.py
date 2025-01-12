import shorpy.gears.config.config as config
import shorpy.gears.logs.setup as log_setup
from shorpy.gears.db.gear import DBGear

cfg, err = config.load()
if err is not None:
    print("configuration loading failed")
    print(err)
    exit(1)

log_setup.setup_logger(cfg.env)

db_gear = DBGear(str(cfg.postgres.dsn))
