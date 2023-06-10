import os
import json
from dotenv import load_dotenv
from queries import execute_query, SUSHISWAP_POOLS_GNOSIS_QUERY, UNISWAP_V3_POOLS_QUERY

load_dotenv()

def generate_ethereum_token_mapping():
    try:
        # Create the basic prompts
        token_map = {}
        # Get the top pools by cumulative volume
        uniswap_result = execute_query(os.environ['UNISWAP_V3_THEGRAPH_URL'], UNISWAP_V3_POOLS_QUERY)
        for pool in uniswap_result['liquidityPools']:
            for input_token in pool["inputTokens"]:
                if input_token["symbol"] not in token_map:
                    token_map[input_token["symbol"]] = input_token["id"]
        # Generate the file that will be used to train the model
        with open('prompts/ethereum_tokens.json', 'w') as prompts_file:
            json.dump(token_map, prompts_file)
    except Exception as e:
        print('an error has occurred while generating ethereum tokens mapping: %s' % (str(e), ))

def generate_gnosis_token_mapping():
    try:
        # Create the basic prompts
        token_map = {}
        # Get the top pools by cumulative volume
        sushiswap_result = execute_query(os.environ['SUSHISWAP_GNOSIS_THEGRAPH_URL'], SUSHISWAP_POOLS_GNOSIS_QUERY)
        for pool in sushiswap_result['liquidityPools']:
            for input_token in pool["inputTokens"]:
                if input_token["symbol"] not in token_map:
                    token_map[input_token["symbol"]] = input_token["id"]
        # Generate the file that will be used to train the model
        with open('prompts/gnosis_tokens.json', 'w') as prompts_file:
            json.dump(token_map, prompts_file)
    except Exception as e:
        print('an error has occurred while generating gnosis tokens mapping: %s' % (str(e), ))

def generate_gnosis_tokens_approval():
    try:
        # Create the basic prompts
        prompts = []
        token_map = {}
        # Get the top pools by cumulative volume
        sushiswap_result = execute_query(os.environ['SUSHISWAP_GNOSIS_THEGRAPH_URL'], SUSHISWAP_POOLS_GNOSIS_QUERY)
        for pool in sushiswap_result['liquidityPools']:
            for input_token in pool["inputTokens"]:
                if input_token["id"] not in token_map:
                    token_map[input_token["id"]] = input_token
                    prompts.append({
                        "prompt": "I want to approve %s spending for address 0xFe8e15ae884524eFfc2fe91dF6f5BA40D8533A92 on Gnosis" % (input_token["symbol"], ),
                    })
        # Generate the file that will be used to train the model
        with open('prompts/gnosis_tokens_approve_prompts.json', 'w') as prompts_file:
            json.dump(prompts, prompts_file)
    except Exception as e:
        print('an error has occurred while generating gnosis tokens approval prompts: %s' % (str(e), ))

def generate_gnosis_tokens_transfer():
    try:
        # Create the basic prompts
        prompts = []
        token_map = {}
        # Get the top pools by cumulative volume
        sushiswap_result = execute_query(os.environ['SUSHISWAP_GNOSIS_THEGRAPH_URL'], SUSHISWAP_POOLS_GNOSIS_QUERY)
        for pool in sushiswap_result['liquidityPools']:
            for input_token in pool["inputTokens"]:
                if input_token["id"] not in token_map:
                    token_map[input_token["id"]] = input_token
                    prompts.append({
                        "prompt": "I want to send or transfer 100 %s to 0xFe8e15ae884524eFfc2fe91dF6f5BA40D8533A92 on Gnosis" % (input_token["symbol"], ),
                    })
        # Generate the file that will be used to train the model
        with open('prompts/gnosis_tokens_transfer_prompts.json', 'w') as prompts_file:
            json.dump(prompts, prompts_file)
    except Exception as e:
        print('an error has occurred while generating gnosis tokens transfer prompts: %s' % (str(e), ))


def generate_gnosis_tokens_balance():
    try:
        # Create the basic prompts
        prompts = []
        token_map = {}
        # Get the top pools by cumulative volume
        sushiswap_result = execute_query(os.environ['SUSHISWAP_GNOSIS_THEGRAPH_URL'], SUSHISWAP_POOLS_GNOSIS_QUERY)
        for pool in sushiswap_result['liquidityPools']:
            for input_token in pool["inputTokens"]:
                if input_token["id"] not in token_map:
                    token_map[input_token["id"]] = input_token
                    prompts.append({
                        "prompt": "I want to know the %s balance of 0xFe8e15ae884524eFfc2fe91dF6f5BA40D8533A92 on Gnosis" % (input_token["symbol"], ),
                        
                    })
        # Generate the file that will be used to train the model
        with open('prompts/gnosis_tokens_balance_prompts.json', 'w') as prompts_file:
            json.dump(prompts, prompts_file)
    except Exception as e:
        print('an error has occurred while generating gnosis tokens balance prompts: %s' % (str(e), ))

generate_ethereum_token_mapping()
generate_gnosis_token_mapping()
generate_gnosis_tokens_approval()
generate_gnosis_tokens_transfer()
generate_gnosis_tokens_balance()