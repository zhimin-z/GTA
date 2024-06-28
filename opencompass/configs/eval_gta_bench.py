from lagent.agents import ReAct
from mmengine.config import read_base

from opencompass.models import OpenAI, Qwen, Gemini
from opencompass.models.lagent import LagentAgent
from opencompass.partitioners import SizePartitioner
from opencompass.runners import LocalRunner
from opencompass.tasks import OpenICLInferTask

with read_base():
    from .datasets.gta_bench import gta_bench_datasets as datasets


models = [
    # dict(
    #     abbr='gpt-4-1106',
    #     type=LagentAgent,
    #     agent_type=ReWOO,
    #     max_turn=10,
    #     llm=dict(
    #         type=OpenAI,
    #         path='gpt-4-1106-preview',
    #         key=None, # put your key here
    #         query_per_second=1,
    #         max_seq_len=4096,
    #         retry=10
    #     ),
    #     # tool_server='http://10.140.0.186:16181',
    #     tool_meta='data/gta/toolmeta.json',
    #     batch_size=8,
    # ),
    # dict(
    #     abbr='gpt-4-0125',
    #     type=LagentAgent,
    #     agent_type=ReAct,
    #     max_turn=10,
    #     llm=dict(
    #         type=OpenAI,
    #         path='gpt-4-0125-preview',
    #         key='alles', 
    #         query_per_second=1,
    #         max_seq_len=4096,
    #         retry=10
    #     ),
    #     # tool_server='http://10.140.0.186:16181',
    #     tool_meta='data/gta_dataset/toolmeta.json',
    #     batch_size=8,
    # ),
    # dict(
    #     abbr='gpt-4o',
    #     type=LagentAgent,
    #     agent_type=ReAct,
    #     max_turn=10,
    #     llm=dict(
    #         type=OpenAI,
    #         path='gpt-4o',
    #         key=None, # put your key here 
    #         query_per_second=1,
    #         max_seq_len=4096,
    #         retry=10
    #     ),
    #     # tool_server='http://10.140.0.138:16181',
    #     tool_meta='data/gta_dataset/toolmeta.json',
    #     batch_size=8,
    # ),
    # dict(
    #     abbr='gpt-3.5-turbo',
    #     type=LagentAgent,
    #     agent_type=ReAct,
    #     max_turn=10,
    #     llm=dict(
    #         type=OpenAI,
    #         path='gpt-3.5-turbo',
    #         key=None, # put your key here
    #         query_per_second=1,
    #         max_seq_len=4096,
    #         retry=10
    #     ),
    #     # tool_server='http://10.140.0.138:16181',
    #     tool_meta='data/gta_dataset/toolmeta.json',
    #     batch_size=8,
    # ),
    # dict(
    #     abbr='claude-3-opus',
    #     type=LagentAgent,
    #     agent_type=ReAct,
    #     max_turn=10,
    #     llm=dict(
    #         type=OpenAI,
    #         path='claude-3-opus',
    #         key=None, # put your key here
    #         query_per_second=1,
    #         max_seq_len=4096,
    #         retry=10
    #     ),
    #     # tool_server='http://10.140.0.138:16181',
    #     tool_meta='data/gta_dataset/toolmeta.json',
    #     batch_size=8,
    # ),
    # dict(
    #     abbr='mistral-large-latest',
    #     type=LagentAgent,
    #     agent_type=ReAct,
    #     max_turn=10,
    #     llm=dict(
    #         type=OpenAI,
    #         path='mistral-large-latest',
    #         key=None, # put your key here
    #         query_per_second=1,
    #         max_seq_len=4096,
    #         retry=10
    #     ),
    #     # tool_server='http://10.140.0.138:16181',
    #     tool_meta='data/gta_dataset/toolmeta.json',
    #     batch_size=8,
    # ),
    #  dict(
    #      abbr='qwen1.5-72b-chat',
    #      type=LagentAgent,
    #      agent_type=ReAct,
    #      max_turn=10,
    #      llm=dict(
    #          type=OpenAI,
    #          path='qwen1.5-72b',
    #          key='EMPTY',
    #          openai_api_base='http://10.140.1.175:12601/v1/chat/completions',
    #          query_per_second=1,
    #          max_seq_len=4096,
    #          stop='<|im_end|>',
    #      ),
    #     #  tool_server='http://10.140.0.138:16181',
    #      tool_meta='data/gta_dataset/toolmeta.json',
    #      batch_size=8,
    #  ),
    # dict(
    #      abbr='qwen1.5-14b',
    #      type=LagentAgent,
    #      agent_type=ReAct,
    #      max_turn=10,
    #      llm=dict(
    #          type=OpenAI,
    #          path='qwen1.5-14b',
    #          key='EMPTY',
    #          openai_api_base='http://10.140.0.158:12581/v1/chat/completions',
    #          query_per_second=1,
    #          max_seq_len=4096,
    #          stop='<|im_end|>',
    #      ),
    #     #  tool_server='http://10.140.0.138:16181',
    #      tool_meta='data/gta_dataset/toolmeta.json',
    #      batch_size=8,
    #  ),
    dict(
            abbr='qwen1.5-7b-chat',
            type=LagentAgent,
            agent_type=ReAct,
            max_turn=10,
            llm=dict(
                type=OpenAI,
                path='qwen1.5-7b-chat',
                key='EMPTY',
                openai_api_base='http://10.140.1.17:12580/v1/chat/completions',
                query_per_second=1,
                max_seq_len=4096,
                stop='<|im_end|>',
            ),
        #  tool_server='http://10.140.0.138:16181',
            tool_meta='data/gta_dataset/toolmeta.json',
            batch_size=8,
        ),
    #  dict(
    #      abbr='mixtral-8x7b-instruct',
    #      type=LagentAgent,
    #      agent_type=ReAct,
    #      max_turn=10,
    #      llm=dict(
    #          type=OpenAI,
    #          path='mixtral-8x7b-instruct',
    #          key='EMPTY',
    #          openai_api_base='http://10.140.1.168:12600/v1/chat/completions',
    #          query_per_second=1,
    #          max_seq_len=4096,
    #      ),
    #      tool_server='http://10.140.0.168:16181',
    #     #  tool_meta='data/gta_dataset/toolmeta.json',
    #      batch_size=8,
    #  ),
    #  dict(
    #      abbr='deepseek-llm-67b-chat',
    #      type=LagentAgent,
    #      agent_type=ReAct,
    #      max_turn=10,
    #      llm=dict(
    #          type=OpenAI,
    #          path='deepseek-llm-67b-chat',
    #          key='EMPTY',
    #          openai_api_base='http://10.140.0.201:12602/v1/chat/completions',
    #          query_per_second=1,
    #          max_seq_len=4096,
    #      ),
    #     #  tool_server='http://10.140.0.162:16181',
    #      tool_meta='data/gta_dataset/toolmeta.json',
    #      batch_size=8,
    #  ),
    # dict(
    #      abbr='llama3-70b-instruct',
    #      type=LagentAgent,
    #      agent_type=ReAct,
    #      max_turn=10,
    #      llm=dict(
    #          type=OpenAI,
    #          path='llama3-70b-instruct',
    #          key='EMPTY',
    #          openai_api_base='http://10.140.1.52:12586/v1/chat/completions',
    #          query_per_second=1,
    #          max_seq_len=4096,
    #      ),
    #      tool_server='http://10.140.0.138:16181',
    #     #  tool_meta='data/gta_dataset/toolmeta.json',
    #      batch_size=8,
    #  ),
    #  dict(
    #      abbr='mistral-7b-instruct',
    #      type=LagentAgent,
    #      agent_type=ReAct,
    #      max_turn=10,
    #      llm=dict(
    #          type=OpenAI,
    #          path='mistral-7b-instruct',
    #          key='EMPTY',
    #          openai_api_base='http://10.140.0.158:12587/v1/chat/completions',
    #          query_per_second=1,
    #          max_seq_len=4096,
    #          retry=10
    #      ),
    #      tool_server='http://10.140.0.186:16181',
    #     #  tool_meta='data/gta_dataset/toolmeta.json',
    #      batch_size=8,
    #  ),
    #  dict(
    #      abbr='deepseek-7b-chat',
    #      type=LagentAgent,
    #      agent_type=ReAct,
    #      max_turn=10,
    #      llm=dict(
    #          type=OpenAI,
    #          path='deepseek-llm-7b-chat',
    #          key='EMPTY',
    #          openai_api_base='http://10.140.1.13:12595/v1/chat/completions',
    #          query_per_second=1,
    #          max_seq_len=4096,
    #      ),
    #     #  tool_server='http://10.140.0.186:16181',
    #      tool_meta='data/gta_dataset/toolmeta.json',
    #      batch_size=8,
    #  ),
    #  dict(
    #      abbr='yi-34b',
    #      type=LagentAgent,
    #      agent_type=ReAct,
    #      max_turn=10,
    #      llm=dict(
    #          type=OpenAI,
    #          path='yi-34b',
    #          key='EMPTY',
    #          openai_api_base='http://10.140.1.13:12593/v1/chat/completions',
    #          query_per_second=1,
    #          max_seq_len=4096,
    #      ),
    #     #  tool_server='http://10.140.0.162:16181',
    #      tool_meta='data/gta_dataset/toolmeta.json',
    #      batch_size=8,
    #  ),
    # dict(
    #      abbr='llama3-8b',
    #      type=LagentAgent,
    #      agent_type=ReAct,
    #      max_turn=10,
    #      llm=dict(
    #          type=OpenAI,
    #          path='llama3-8b-instruct',
    #          key='EMPTY',
    #          openai_api_base='http://10.140.1.52:12586/v1/chat/completions',
    #          query_per_second=1,
    #          max_seq_len=4096,
    #      ),
    #      tool_server='http://10.140.0.138:16181',
    #     #  tool_meta='data/gta_dataset/toolmeta.json',
    #      batch_size=8,
    #  ),
    #  dict(
    #      abbr='yi-6b',
    #      type=LagentAgent,
    #      agent_type=ReAct,
    #      max_turn=10,
    #      llm=dict(
    #          type=OpenAI,
    #          path='yi-6b',
    #          key='EMPTY',
    #          openai_api_base='http://10.140.1.13:12592/v1/chat/completions',
    #          query_per_second=1,
    #          max_seq_len=4096,
    #      ),
    #     #  tool_server='http://10.140.0.162:16181',
    #      tool_meta='data/gta_dataset/toolmeta.json',
    #      batch_size=8,
    #  ),
    # dict(
    #      abbr='glm-4-9b-chat',
    #      type=LagentAgent,
    #      agent_type=ReAct,
    #      max_turn=10,
    #      llm=dict(
    #          type=OpenAI,
    #          path='glm-4-9b-chat',
    #          key='EMPTY',
    #          openai_api_base='http://10.140.0.212:12605/v1/chat/completions',
    #          query_per_second=1,
    #          max_seq_len=4096,
    #      ),
    #     #  tool_server='http://10.140.0.162:16181',
    #      tool_meta='data/gta_dataset/toolmeta.json',
    #      batch_size=8,
    #  ),
    #  dict(
    #      abbr='qwen2-7b-instruct',
    #      type=LagentAgent,
    #      agent_type=ReAct,
    #      max_turn=10,
    #      llm=dict(
    #          type=OpenAI,
    #          path='qwen2-7b-instruct',
    #          key='EMPTY',
    #          openai_api_base='http://10.140.1.172:12606/v1/chat/completions',
    #          query_per_second=1,
    #          max_seq_len=4096,
    #      ),
    #      tool_server='http://10.140.1.13:16181',
    #     #  tool_meta='data/gta_dataset/toolmeta.json',
    #      batch_size=8,
    #  ),
    #  dict(
    #      abbr='qwen2-72b-instruct',
    #      type=LagentAgent,
    #      agent_type=ReAct,
    #      max_turn=10,
    #      llm=dict(
    #          type=OpenAI,
    #          path='qwen2-72b-instruct',
    #          key='EMPTY',
    #          openai_api_base='http://10.140.0.212:12607/v1/chat/completions',
    #          query_per_second=1,
    #          max_seq_len=4096,
    #      ),
    #      tool_server='http://10.140.1.13:16181',
    #     #  tool_meta='data/gta_dataset/toolmeta.json',
    #      batch_size=8,
    #  ),
]


infer = dict(
    partitioner=dict(type=SizePartitioner, max_task_size=50, gen_task_coef=1),
    runner=dict(type=LocalRunner, task=dict(type=OpenICLInferTask)),
)
