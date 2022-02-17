import yaml
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some logits.')
    parser.add_argument('--num', type=int)
    args = parser.parse_args()
    num = args.num
    yamlFile = "configs/benchmark/ucf/8at16-fold1.yaml"
    cfg = yaml.safe_load(open(yamlFile, 'rb'))
    cfg['optimizer']['num_epochs'] = num
    open(yamlFile, 'w').write(yaml.dump(cfg))
