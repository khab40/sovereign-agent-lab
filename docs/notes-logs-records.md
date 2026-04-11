1. HAPPY PATH

(sovereign-agent-lab) akhabalov-da@AKHABALOV-MB sovereign-agent-lab % make ex3-chat
Exercise 3 — Rasa Chat
Make sure 'make ex3-actions' is running in another terminal first.

Conversation scripts to run:
  1. Happy path:     'calling to confirm a booking' → 160 guests → ~50 vegan → £200 deposit
  2. Deposit too high: same flow, but use a deposit above £300
  3. Out of scope:   mid-conversation ask about parking or AV equipment

CALM note: the LLM understands 'about 160 people' or 'one-sixty' as 160.
No regex needed — that's the from_llm slot mapping at work.

Copy-paste your terminal output into week1/answers/ex3_answers.py

cd exercise3_rasa && uv run rasa shell
warning: `VIRTUAL_ENV=/Users/akhabalov-da_1/Documents/STUDY/nebius-ai-performance-engineering/code/sovereign-agent-lab/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
Uninstalled 2 packages in 12ms
Installed 2 packages in 3ms
2026-04-09 10:23:08 INFO     rasa.tracing.backend_tracing_config  - [info     ] No backend tracing configuration found in endpoints.yml. Supported backend tracing types are 'jaeger' and 'otlp'. Backend tracing will not be configured. event_key=endpoint.read.no_backend_tracing_config filename=/Users/akhabalov-da_1/Documents/STUDY/nebius-ai-performance-engineering/code/sovereign-agent-lab/exercise3_rasa/endpoints.yml
2026-04-09 10:23:10 INFO     root  - Starting Rasa server on http://0.0.0.0:5005
2026-04-09 10:23:10 INFO     rasa.core.processor  - [info     ] Loading model.                 event_key=rasa.core.processor.load_model model_path=models/20260409-081101-chromatic-pixel.tar.gz
2026-04-09 10:23:11 INFO     rasa.shared.core.domain  - [info     ] domain.from_yaml.validating   
2026-04-09 10:23:11 WARNING  rasa.shared.utils.llm  - [warning  ] The LLM_API_HEALTH_CHECK environment variable is set to false, which will disable LLM health check. It is recommended to set this variable to true in production environments. event_key=llm_based_command_generator.load.perform_llm_health_check.disabled
2026-04-09 10:23:11 INFO     rasa.dialogue_understanding.generator.llm_based_command_generator  - [info     ] llm_based_command_generator.flow_retrieval.enabled
2026-04-09 10:23:11 WARNING  rasa.shared.utils.llm  - [warning  ] The LLM_API_HEALTH_CHECK environment variable is set to false, which will disable embeddings API health check. It is recommended to set this variable to true in production environments. event_key=flow_retrieval.load.perform_embeddings_health_check.disabled
2026-04-09 10:23:11 INFO     faiss.loader  - Loading faiss.
2026-04-09 10:23:11 INFO     faiss.loader  - Successfully loaded faiss.
2026-04-09 10:23:11 INFO     rasa.shared.core.domain  - [info     ] domain.from_yaml.validating   
2026-04-09 10:23:11 WARNING  rasa.validator  - [warning  ] Default pattern flows include responses with rephrasing enabled, but the NLG endpoint is not configured in endpoints.yml. Rephrasing for default patterns will be skipped. event_key=validator.verify_rephrase_endpoints_consistency.defaults_only_rephrase_without_nlg
2026-04-09 10:23:11 INFO     root  - Rasa server is up and running.
Bot loaded. Type a message and press enter (use '/stop' to exit): 
Your input ->  40                                               

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

How many guests are you confirming for tonight's event?
Your input ->  120 guests.                                                                             

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

And how many of those guests will need vegan meals?
Your input ->  20.                                                                                     

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

What deposit amount in GBP are you proposing to secure the booking?
Your input ->  250 pounds.                                                                             

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers
Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Thank you — booking confirmed. 120 guests, 20 requiring vegan meals, £250 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
Your input ->  exit                                                                                    
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Is there anything else I can help you with?
Your input ->  no                                                                                      
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Is there anything else I can help you with?
Your input ->                                                                                          

Cancelled by user

2026-04-09 10:25:16 INFO     root  - Killing Sanic server now.
2026-04-09 10:25:16 INFO     sanic.server  - Starting worker [22423]
2026-04-09 10:25:16 INFO     sanic.server  - Stopping worker [22423]
2026-04-09 10:25:17 ERROR    asyncio  - Fatal error on SSL transport
protocol: <asyncio.sslproto.SSLProtocol object at 0x12bc30a60>
transport: <_SelectorSocketTransport closing fd=16>
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/selector_events.py", line 918, in write
    n = self._sock.send(data)
OSError: [Errno 9] Bad file descriptor

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/sslproto.py", line 684, in _process_write_backlog
    self._transport.write(chunk)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/selector_events.py", line 924, in write
    self._fatal_error(exc, 'Fatal write error on socket transport')
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/selector_events.py", line 719, in _fatal_error
    self._force_close(exc)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/selector_events.py", line 731, in _force_close
    self._loop.call_soon(self._call_connection_lost, exc)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/base_events.py", line 745, in call_soon
    self._check_closed()
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/base_events.py", line 510, in _check_closed
    raise RuntimeError('Event loop is closed')
RuntimeError: Event loop is closed

2. Deposit too high
(sovereign-agent-lab) akhabalov-da@AKHABALOV-MB sovereign-agent-lab % make ex3-chat
Exercise 3 — Rasa Chat
Make sure 'make ex3-actions' is running in another terminal first.

Conversation scripts to run:
  1. Happy path:     'calling to confirm a booking' → 160 guests → ~50 vegan → £200 deposit
  2. Deposit too high: same flow, but use a deposit above £300
  3. Out of scope:   mid-conversation ask about parking or AV equipment

CALM note: the LLM understands 'about 160 people' or 'one-sixty' as 160.
No regex needed — that's the from_llm slot mapping at work.

Copy-paste your terminal output into week1/answers/ex3_answers.py

cd exercise3_rasa && uv run rasa shell
warning: `VIRTUAL_ENV=/Users/akhabalov-da_1/Documents/STUDY/nebius-ai-performance-engineering/code/sovereign-agent-lab/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
Uninstalled 2 packages in 10ms
Installed 2 packages in 3ms
2026-04-09 10:26:48 INFO     rasa.tracing.backend_tracing_config  - [info     ] No backend tracing configuration found in endpoints.yml. Supported backend tracing types are 'jaeger' and 'otlp'. Backend tracing will not be configured. event_key=endpoint.read.no_backend_tracing_config filename=/Users/akhabalov-da_1/Documents/STUDY/nebius-ai-performance-engineering/code/sovereign-agent-lab/exercise3_rasa/endpoints.yml
2026-04-09 10:26:50 INFO     root  - Starting Rasa server on http://0.0.0.0:5005
2026-04-09 10:26:51 INFO     rasa.core.processor  - [info     ] Loading model.                 event_key=rasa.core.processor.load_model model_path=models/20260409-081101-chromatic-pixel.tar.gz
2026-04-09 10:26:51 INFO     rasa.shared.core.domain  - [info     ] domain.from_yaml.validating   
2026-04-09 10:26:51 WARNING  rasa.shared.utils.llm  - [warning  ] The LLM_API_HEALTH_CHECK environment variable is set to false, which will disable LLM health check. It is recommended to set this variable to true in production environments. event_key=llm_based_command_generator.load.perform_llm_health_check.disabled
2026-04-09 10:26:51 INFO     rasa.dialogue_understanding.generator.llm_based_command_generator  - [info     ] llm_based_command_generator.flow_retrieval.enabled
2026-04-09 10:26:51 WARNING  rasa.shared.utils.llm  - [warning  ] The LLM_API_HEALTH_CHECK environment variable is set to false, which will disable embeddings API health check. It is recommended to set this variable to true in production environments. event_key=flow_retrieval.load.perform_embeddings_health_check.disabled
2026-04-09 10:26:51 INFO     faiss.loader  - Loading faiss.
2026-04-09 10:26:51 INFO     faiss.loader  - Successfully loaded faiss.
2026-04-09 10:26:51 INFO     rasa.shared.core.domain  - [info     ] domain.from_yaml.validating   
2026-04-09 10:26:51 WARNING  rasa.validator  - [warning  ] Default pattern flows include responses with rephrasing enabled, but the NLG endpoint is not configured in endpoints.yml. Rephrasing for default patterns will be skipped. event_key=validator.verify_rephrase_endpoints_consistency.defaults_only_rephrase_without_nlg
2026-04-09 10:26:51 INFO     root  - Rasa server is up and running.
Bot loaded. Type a message and press enter (use '/stop' to exit): 
Your input ->  I’m calling to confirm tonight’s booking.                                               

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

How many guests are you confirming for tonight's event?
Your input ->  120.                                                                                    
And how many of those guests will need vegan meals?
Your input ->  20.                                                                                     

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

What deposit amount in GBP are you proposing to secure the booking?
Your input ->  350 pounds.                                                                             
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £350 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?

3. Out of scope
warning: `VIRTUAL_ENV=/Users/akhabalov-da_1/Documents/STUDY/nebius-ai-performance-engineering/code/sovereign-agent-lab/.venv` does not match the project environment path `.venv` and will be ignored; use `--active` to target the active environment instead
Uninstalled 2 packages in 14ms
Installed 2 packages in 5ms
2026-04-09 10:28:23 INFO     rasa.tracing.backend_tracing_config  - [info     ] No backend tracing configuration found in endpoints.yml. Supported backend tracing types are 'jaeger' and 'otlp'. Backend tracing will not be configured. event_key=endpoint.read.no_backend_tracing_config filename=/Users/akhabalov-da_1/Documents/STUDY/nebius-ai-performance-engineering/code/sovereign-agent-lab/exercise3_rasa/endpoints.yml
2026-04-09 10:28:25 INFO     root  - Starting Rasa server on http://0.0.0.0:5005
2026-04-09 10:28:26 INFO     rasa.core.processor  - [info     ] Loading model.                 event_key=rasa.core.processor.load_model model_path=models/20260409-081101-chromatic-pixel.tar.gz
2026-04-09 10:28:26 INFO     rasa.shared.core.domain  - [info     ] domain.from_yaml.validating   
2026-04-09 10:28:26 WARNING  rasa.shared.utils.llm  - [warning  ] The LLM_API_HEALTH_CHECK environment variable is set to false, which will disable LLM health check. It is recommended to set this variable to true in production environments. event_key=llm_based_command_generator.load.perform_llm_health_check.disabled
2026-04-09 10:28:26 INFO     rasa.dialogue_understanding.generator.llm_based_command_generator  - [info     ] llm_based_command_generator.flow_retrieval.enabled
2026-04-09 10:28:26 WARNING  rasa.shared.utils.llm  - [warning  ] The LLM_API_HEALTH_CHECK environment variable is set to false, which will disable embeddings API health check. It is recommended to set this variable to true in production environments. event_key=flow_retrieval.load.perform_embeddings_health_check.disabled
2026-04-09 10:28:26 INFO     faiss.loader  - Loading faiss.
2026-04-09 10:28:26 INFO     faiss.loader  - Successfully loaded faiss.
2026-04-09 10:28:26 INFO     rasa.shared.core.domain  - [info     ] domain.from_yaml.validating   
2026-04-09 10:28:26 WARNING  rasa.validator  - [warning  ] Default pattern flows include responses with rephrasing enabled, but the NLG endpoint is not configured in endpoints.yml. Rephrasing for default patterns will be skipped. event_key=validator.verify_rephrase_endpoints_consistency.defaults_only_rephrase_without_nlg
2026-04-09 10:28:26 INFO     root  - Rasa server is up and running.
Bot loaded. Type a message and press enter (use '/stop' to exit): 
Your input ->  I’m calling to confirm tonight’s booking.                                               

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

Provider List: https://docs.litellm.ai/docs/providers



Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

How many guests are you confirming for tonight's event?
Your input ->  120.                                                                                    

Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers


Provider List: https://docs.litellm.ai/docs/providers

And how many of those guests will need vegan meals?
Your input ->  Before that, is there parking nearby?                                                   
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
Your input ->  Do you have AV equipment?                                                               
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking?
Your input ->    

First runs of ex4 did not provide any evidence - no tool calls. smae results. patching code to get tools calls and to see the difference. 

