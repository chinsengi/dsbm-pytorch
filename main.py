import os
import hydra


@hydra.main(config_path="conf", config_name="config", version_base=None)
def main(cfg):
    if cfg.Method == "DSB":
        from run_dsb import run
    elif cfg.Method == "DBDSB":
        from run_dbdsb import run
    elif cfg.Method == "RF":
        from run_rf import run
    else: 
        raise NotImplementedError
    return run(cfg)

if __name__ == "__main__":
    main()