import json
import uuid


def read_write_json(read_file_path, cus_file_path, pro_file_path):
    customer_list = []
    project_list = []

    # open json file
    with open(read_file_path, encoding="utf-8") as read_json_file:
        file_contents = json.load(read_json_file)

        # loop through the file_contents
        # parse them and fill up both customer
        # and project list
        print("Processing file contents...")
        for content in file_contents:
            customer_id = uuid.uuid4()
            project_id = uuid.uuid4()

            customer = {
                "name": content["customer"],
                "customer_id": str(customer_id),
                "url": ""
            }

            project = {
                "project_id": str(project_id),
                "project_name": content["project_name"],
                "project_details": content["project_details"],
                "problem_details": content["problem_details"],
                "solution_details": content["solution_details"],
                "impact": content["impact"],
                "css_impact_story": content["css_impact_story"],
                "logo_usage_right": content["logo_usage_right"],
                "public_ref_right": content["public_ref_right"],
                "case_material_url": content["case_material_url"],
                "category": content["category"],
                "customer_contact": content["customer_contact"],
                "qvik_dev_lead": content["qvik_dev_lead"],
                "qvik_sales_lead": content["qvik_sales_lead"],
                "start_date": content["start_date"],
                "end_date": content["end_date"],
                "deal_type": content["deal_type"],
                "public_customer": content["public_customer"],
                "cloud_products": content["cloud_products"],
                "cloud_platform": content["cloud_platform"],
                "technology": content["technology"],
                "description": content["description"],
                "customer_id": str(customer_id)
            }

            customer_list.append(customer)
            project_list.append(project)

    with open(cus_file_path, "w", encoding="utf-8") as cus_list_json:
        cus_list_json.write(json.dumps(customer_list, indent=4))

    with open(pro_file_path, "w", encoding="utf-8") as pro_list_json:
        pro_list_json.write(json.dumps(project_list, indent=4))

    print("finished processing!")


# call read_write_json function with file name
read_write_json("Backend_cases_list.json", "cus_list.json", "pro_list.json")
