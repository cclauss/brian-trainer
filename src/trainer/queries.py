import os
import requests
from dotenv import load_dotenv

load_dotenv()

UNISWAP_V3_POOLS_QUERY = """
query GetUniswapV3Pools {   
    liquidityPools(first: 50, orderBy: totalValueLockedUSD, orderDirection: desc) {
        inputTokens {
            id
            name
            symbol
        }
        totalValueLockedUSD
    }
}
"""

SUSHISWAP_POOLS_GNOSIS_QUERY = """
query GetSushiswapGnosisPools($first: Int!, $skip: Int!) {
  liquidityPools(first: $first, skip: $skip, orderBy: cumulativeVolumeUSD, orderDirection: desc) {
    cumulativeVolumeUSD
    inputTokens {
      id
      decimals
      name
      symbol
    }
  }
}
"""


def execute_query(endpoint: str, query: str, variables: dict = {}) -> dict:
    response = requests.post(
        endpoint.replace('[api-key]', os.environ['THEGRAPH_API_KEY']),
        json={"query": query, "variables": variables},
    )
    response.raise_for_status()
    return response.json()["data"]