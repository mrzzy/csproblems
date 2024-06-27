#
# CSProblems
# Leetcode
# 721. Accounts Merge
#

from typing import List, Set


class Account:
    def __init__(self, name: str, email: str, connected: list["Account"]):
        self.name = name
        self.email = email
        self.connected = connected

    def __hash__(self):
        return hash(self.email)

    def __repr__(self):
        return self.email


def build_graph(accounts: List[List[str]]) -> List[Account]:
    # mapping of email -> account with that email
    email_account = {}
    # build graph of users accounts
    for emails in accounts:
        # collects accounts for each user
        user_accounts = []
        name = emails[0]
        for email in emails[1:]:
            account = email_account.get(email, Account(name, email, []))
            email_account[email] = account
            user_accounts.append(account)

        # strongly connect all accounts in the same account list
        for i in range(len(user_accounts)):
            for j in range(i + 1, len(user_accounts)):
                user_accounts[i].connected.append(user_accounts[j])
                user_accounts[j].connected.append(user_accounts[i])

    return list(email_account.values())


def connected_to(account: Account, seen: Set[Account]) -> Set[Account]:
    """Get all accounts connected to the given account"""
    if account in seen:
        return seen
    # perform recursive dfs to find connected components
    seen.add(account)Î
    for adjacent in account.connected:
        connected_to(adjacent, seen)
    return seen


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        merged_accounts = []
        graph, seen = build_graph(accounts), set()
        for account in graph:
            if account in seen:
                continue
            # all accounts connected to the current account belong to the same user
            user_accounts = connected_to(account, set())
            user_accounts = sorted(user_accounts, key=lambda a: a.email)
            merged_accounts.append(
                [account.name] + [account.email for account in user_accounts]
            )
            seen.update(user_accounts)

        return merged_accounts
