from typing import List

# https://leetcode.com/problems/unique-email-addresses/

def num_unique_emails(emails: List[str]) -> int:
    # Add emails list to a set to count the unique emails after santizing them
    emails_set = set()

    for email in emails:
        # split the email by @ to get local name
        local_name, domain_name = email.split("@")

        # remove the .
        local_name = local_name.replace(".", "")

        # remove the anything after +
        if "+" in local_name:
            local_name = local_name[0:local_name.index("+")]

        email = local_name + "@" + domain_name

        emails_set.add(email)

    return len(emails_set)

print(num_unique_emails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
# 2

print(num_unique_emails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
# 2