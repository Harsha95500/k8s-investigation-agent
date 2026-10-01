# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

from app.tools.kubernetes import (
    get_deployment_details,
    get_deployments,
    get_events,
    get_node_details,
    get_nodes,
    get_pod_details,
    get_pod_logs,
    get_pods,
    get_service_details,
    get_services,
)


MODEL = "gemini-3.8-flash"


root_agent = Agent(
    # Keep in sync with agents-cli-manifest.yaml.
    name="k8s_investigator",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""
You are a Kubernetes investigation assistant.

Your job is to investigate Kubernetes resources using the available
read-only tools.

Use the Kubernetes tools to obtain current information rather than
guessing.

When investigating an issue, gather relevant evidence from multiple
Kubernetes resources when appropriate.

Clearly explain the evidence returned by Kubernetes.

Do not claim to have investigated a resource unless you actually
used the appropriate tool.

You are currently a read-only investigation agent.

Do not perform destructive Kubernetes operations.
Do not delete, modify, restart, scale, patch, or apply Kubernetes
resources.
""",
    tools=[
        get_pods,
        get_pod_logs,
        get_pod_details,
        get_events,
        get_deployments,
        get_deployment_details,
        get_services,
        get_service_details,
        get_nodes,
        get_node_details,
    ],
)


app = App(
    root_agent=root_agent,
    name="app",
)