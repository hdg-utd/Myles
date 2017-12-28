import json

class DomainFinder:
    @staticmethod
    def get_domain_name(company):
        pass
        with open('./common/domain_list.json', 'r+') as f:
            domain_data = json.load(f)
            if company in domain_data:
                return domain_data[company]
            else:
                domain_data[company] = "Test" #fetch from google
                f.write(json.dumps(domain_data))
