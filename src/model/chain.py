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
            examples=[("I want to know the balance", "balance")],
        ),
        Text(
            id="address",
            description="The destination address",
            examples=[("I want to know the wstETH balance of 0xFe8e15ae884524eFfc2fe91dF6f5BA40D8533A92 on Gnosis", 
                       "0xFe8e15ae884524eFfc2fe91dF6f5BA40D8533A92")],
        ),
        Text(
            id="amount",
            description= "the amount I want to transfer",
            examples = [("I want to send or transfer 100 WETH to 0xFe8e15ae884524eFfc2fe91dF6f5BA40D8533A92 on Gnosis", "100")]
        ),
        Text(
            id="token",
            description="The token of reference or the transacton",
            examples=[("I want to know the wstETH balance of 0xFe8e15ae884524eFfc2fe91dF6f5BA40D8533A92 on Gnosis", 
                       "wstETH")],
        ),
        Text(
            id="chain",
            description="The reference chain on which to perform the action",
            examples=[("I want to know the COSMO balance of 0xFe8e15ae884524eFfc2fe91dF6f5BA40D8533A92 on Gnosis", "Gnosis")],
        ),
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