from langchain.chat_models import ChatOpenAI
from kor.extraction import create_extraction_chain
from kor.nodes import Object, Text
from kor import create_extraction_chain
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    #model_name="gpt-3.5-turbo",
    temperature=0,
)

schema = Object(
    id="brian",
    description="The Brian AI langchain schema",
    attributes=[
        Text(
            id="action",
            description="what is the action that the user wants to perform",
            examples=[("I want to know the balance", "balance"), ("I want to swap", "swap"), ("I want to transfer", "transfer"), ("I want to send", "send"), ("I want to know the total supply", "total supply"), ("I want to swap", "swap")],
        ),
        Text(
            id="address",
            description="The destination address",
            examples=[("I want to know the wstETH balance of 0xFe8e15ae884524eFfc2fe91dF6f5BA40D8533A92 on Gnosis", "0xFe8e15ae884524eFfc2fe91dF6f5BA40D8533A92")],
        ),
        Text(
            id="amount",
            description= "the amount I want to transfer or swap",
            examples = [("I want to send or transfer 100 WETH to 0xFe8e15ae884524eFfc2fe91dF6f5BA40D8533A92 on Gnosis", "100"), ("I want to swap 150 XDAI for DAI on Gnosis", "150")]
        ),
        Text(
            id="token",
            description="The token of reference or the transacton",
            examples=[("I want to know the wstETH balance of 0xFe8e15ae884524eFfc2fe91dF6f5BA40D8533A92 on Gnosis", "wstETH"), ("What is the GNO total supply on Gnosis", "GNO"), ("I want to know the GNO total supply on Gnosis", "GNO"), ("I want to swap 100 XDAI for DAI on Gnosis", "XDAI")],
        ),
        Text(
            id="chain",
            description="The reference chain on which to perform the action",
            examples=[("I want to know the COSMO balance of 0xFe8e15ae884524eFfc2fe91dF6f5BA40D8533A92 on Gnosis", "Gnosis"), ("I want to swap 150 XDAI for DAI on Gnosis", "Gnosis")],
        ),
        # Text(
        #     id="token1",
        #     description="The token used as input in the swap",
        #     examples=[("I want to swap 100 XDAI for DAI on Gnosis", "XDAI")]
        # ),
        Text(
            id="token_out",
            description="The token used as output in the swap",
            examples=[("I want to swap 100 XDAI for DAI on Gnosis", "DAI")]
        )
    ],
    examples=[
        (
            "I want to know the AAVE balance of 0xFe8e15ae884524eFfc2fe91dF6f5BA40D8533A92 on Gnosis",
            [
                {"action": "balance", "adddress": "0xFe8e15ae884524eFfc2fe91dF6f5BA40D8533A92", "chain": "Gnosis", "token":"AAVE"},
            ],
        )
    ],
    many=True,
)


chain = create_extraction_chain(llm, schema)