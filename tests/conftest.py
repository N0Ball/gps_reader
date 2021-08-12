import yaml

def get_test_data(test_data_path):
    case = []
    test_input = []
    expected = []
    with open(test_data_path) as f:
        dat = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = dat['tests']
        for td in test:
            case.append(td.get('case', ''))
            test_input.append(td.get('test_input', {}))
            expected.append(td.get('expected', {}))
    parameters = zip(case, test_input, expected)
    return case, parameters