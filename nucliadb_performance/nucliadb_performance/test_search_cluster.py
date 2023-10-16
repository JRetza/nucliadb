import asyncio
import random

from faker import Faker
from molotov import global_setup, scenario

from nucliadb_performance.utils import (
    get_fake_word,
    get_random_kb,
    get_search_client,
    load_kbs,
)

fake = Faker()


# These weights have been obtained from grafana in production by looking at
# some time period where we had some traffic and getting the average
# request rate for each endpoint during that time period.
SUGGEST_WEIGHT = 40.4
CATALOG_WEIGHT = 38.4
CHAT_WEIGHT = 10
FIND_WEIGHT = 5.3
SEARCH_WEIGHT = 5.6


@global_setup()
def init_test(args):
    load_kbs()


@scenario(weight=SUGGEST_WEIGHT)
async def test_suggest(session):
    client = get_search_client(session)
    kbid = get_random_kb()
    await client.make_request(
        "GET",
        f"/v1/kb/{kbid}/suggest",
        params={"query": get_fake_word()},
    )


@scenario(weight=CATALOG_WEIGHT)
async def test_catalog(session):
    client = get_search_client(session)
    kbid = get_random_kb()
    await client.make_request(
        "GET",
        f"/v1/kb/{kbid}/catalog",
    )


@scenario(weight=CHAT_WEIGHT)
async def test_chat(session):
    client = get_search_client(session)
    kbid = get_random_kb()
    # To avoid calling the LLM in the performance test, we simulate the
    # chat intraction as a find (the retrieval phase) plus some synthetic
    # sleep time (the LLM answer generation streaming time)
    await client.make_request(
        "POST",
        f"/v1/kb/{kbid}/find",
        json={"query": fake.sentence()},
    )
    sleep_time = abs(random.gauss(2, 1))
    await asyncio.sleep(sleep_time)


@scenario(weight=FIND_WEIGHT)
async def test_find(session):
    client = get_search_client(session)
    kbid = get_random_kb()
    await client.make_request(
        "GET",
        f"/v1/kb/{kbid}/find",
        params={"query": fake.sentence()},
    )


@scenario(weight=SEARCH_WEIGHT)
async def test_search(session):
    client = get_search_client(session)
    kbid = get_random_kb()
    await client.make_request(
        "GET",
        f"/v1/kb/{kbid}/search",
        params={"query": fake.sentence()},
    )
