---
slug: /cli
---

# Dagger CLI

<div class="status-badge">Technical Preview</div>

## What is the Dagger CLI?

The Dagger CLI is an optional tool to interact with the Dagger Engine in different ways. This includes:

* Developing and running CI/CD pipelines from the command-line.
* Proxying requests to the Dagger GraphQL API.
* Executing custom commands in a Dagger session for [building your custom API client](../api/254103-build-custom-client.md) or deeper introspection.

## How does it work?

```mermaid
graph LR;

subgraph program["Your program"]
  lib["Dagger CLI"]
end

engine["Dagger Engine"]
oci["OCI container runtime"]

subgraph A["your build pipeline"]
  A1[" "] -.-> A2[" "] -.-> A3[" "]
end
subgraph B["your test pipeline"]
  B1[" "] -.-> B2[" "] -.-> B3[" "] -.-> B4[" "]
end
subgraph C["your deployment pipeline"]
  C1[" "] -.-> C2[" "] -.-> C3[" "] -.-> C4[" "]
end

lib -..-> engine -..-> oci -..-> A1 & B1 & C1
```

1. Using the Dagger CLI, your program (typically a shell script) opens a new session to a Dagger Engine: either by connecting to an existing engine, or by provisioning one on-the-fly.
2. Using the Dagger CLI, your program prepares API requests describing pipelines to run, then sends them to the engine. The wire protocol used to communicate with the engine is private and not yet documented, but this will change in the future. For now, the Dagger CLI is the only documented interface available to your program.
3. When the engine receives an API request, it computes a [Directed Acyclic Graph (DAG)](https://en.wikipedia.org/wiki/Directed_acyclic_graph) of low-level operations required to compute the result, and starts processing operations concurrently.
4. When all operations in the pipeline have been resolved, the engine sends the pipeline result back to your program.
5. Your program may use the pipeline's result as input to new pipelines.

## Get started

To learn more, [install the Dagger CLI](./465058-install.md) and [start using it](./389936-run-pipelines-cli.md).
