import subprocess


def _run_kubectl(command: list[str]) -> str:
    """Run a read-only kubectl command and return its output.

    Args:
        command: The kubectl command and arguments to execute.

    Returns:
        The command output or an error message.
    """
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=15,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return "kubectl command timed out after 15 seconds."
    except FileNotFoundError:
        return (
            "kubectl was not found. "
            "Make sure kubectl is installed and available in PATH."
        )

    if result.returncode != 0:
        return f"kubectl command failed: {result.stderr.strip()}"

    return result.stdout.strip() or "No results found."


def get_pods(namespace: str = "default") -> str:
    """Get pods running in a Kubernetes namespace.

    Args:
        namespace: The Kubernetes namespace to inspect.

    Returns:
        Current pod information.
    """
    return _run_kubectl(
        ["kubectl", "get", "pods", "-n", namespace]
    )


def get_pod_logs(
    pod_name: str,
    namespace: str = "default",
) -> str:
    """Get logs from a Kubernetes pod.

    Args:
        pod_name: The name of the Kubernetes pod.
        namespace: The Kubernetes namespace containing the pod.

    Returns:
        Logs produced by the pod.
    """
    return _run_kubectl(
        ["kubectl", "logs", pod_name, "-n", namespace]
    )


def get_pod_details(
    pod_name: str,
    namespace: str = "default",
) -> str:
    """Get detailed information about a Kubernetes pod.

    Args:
        pod_name: The name of the Kubernetes pod.
        namespace: The Kubernetes namespace containing the pod.

    Returns:
        Detailed pod information.
    """
    return _run_kubectl(
        ["kubectl", "describe", "pod", pod_name, "-n", namespace]
    )


def get_events(namespace: str = "default") -> str:
    """Get Kubernetes events from a namespace.

    Args:
        namespace: The Kubernetes namespace to inspect.

    Returns:
        Kubernetes events for the namespace.
    """
    return _run_kubectl(
        [
            "kubectl",
            "get",
            "events",
            "-n",
            namespace,
            "--sort-by=.lastTimestamp",
        ]
    )


def get_deployments(namespace: str = "default") -> str:
    """Get deployments in a Kubernetes namespace.

    Args:
        namespace: The Kubernetes namespace to inspect.

    Returns:
        Current deployment information.
    """
    return _run_kubectl(
        ["kubectl", "get", "deployments", "-n", namespace]
    )


def get_deployment_details(
    deployment_name: str,
    namespace: str = "default",
) -> str:
    """Get detailed information about a Kubernetes deployment.

    Args:
        deployment_name: The name of the deployment.
        namespace: The Kubernetes namespace containing the deployment.

    Returns:
        Detailed deployment information.
    """
    return _run_kubectl(
        [
            "kubectl",
            "describe",
            "deployment",
            deployment_name,
            "-n",
            namespace,
        ]
    )


def get_services(namespace: str = "default") -> str:
    """Get services in a Kubernetes namespace.

    Args:
        namespace: The Kubernetes namespace to inspect.

    Returns:
        Current service information.
    """
    return _run_kubectl(
        ["kubectl", "get", "services", "-n", namespace]
    )


def get_service_details(
    service_name: str,
    namespace: str = "default",
) -> str:
    """Get detailed information about a Kubernetes service.

    Args:
        service_name: The name of the Kubernetes service.
        namespace: The Kubernetes namespace containing the service.

    Returns:
        Detailed service information.
    """
    return _run_kubectl(
        [
            "kubectl",
            "describe",
            "service",
            service_name,
            "-n",
            namespace,
        ]
    )


def get_nodes() -> str:
    """Get Kubernetes cluster nodes.

    Returns:
        Current node information.
    """
    return _run_kubectl(
        ["kubectl", "get", "nodes"]
    )


def get_node_details(node_name: str) -> str:
    """Get detailed information about a Kubernetes node.

    Args:
        node_name: The name of the Kubernetes node.

    Returns:
        Detailed node information.
    """
    return _run_kubectl(
        ["kubectl", "describe", "node", node_name]
    )