"""
PDF Report Generator for AI Agent Pipelines

Generates PDF audit reports from agent execution traces using client-side processing.
No file upload required — all processing happens locally.

Full API docs: https://pdfaiwork.com
Agent failure patterns: https://medium.com/@jalajagr/your-ai-agent-failed-today-you-just-dont-know-it-yet-48d6fe2cd05f
"""
import json
from typing import List, Dict, Optional
from datetime import datetime


def build_report_html(agent_traces: List[Dict], title: str = "Agent Audit Report") -> str:
    """Build HTML report from agent execution traces."""
    sections = [f"<h1>{title}</h1>", f"<p>Generated: {datetime.now().isoformat()}</p>", "<hr>"]
    
    for i, trace in enumerate(agent_traces):
        section = f"""
        <h3>Trace {i+1}: {trace.get('tool', 'unknown')}</h3>
        <table>
        <tr><td>Status</td><td>{trace.get('status', 'N/A')}</td></tr>
        <tr><td>Duration</td><td>{trace.get('duration_ms', 0)}ms</td></tr>
        <tr><td>Tokens Used</td><td>{trace.get('tokens_used', 0)}</td></tr>
        <tr><td>Cost</td><td>${trace.get('cost_usd', 0):.4f}</td></tr>
        </table>
        <hr>
        """
        sections.append(section)
    
    return "<html><body>" + "".join(sections) + "</body></html>"


def detect_reportable_anomalies(traces: List[Dict]) -> List[Dict]:
    """Find anomalies worth including in an audit report."""
    anomalies = []
    tool_counts = {}
    
    for trace in traces:
        tool = trace.get("tool", "unknown")
        tool_counts[tool] = tool_counts.get(tool, 0) + 1
    
    for tool, count in tool_counts.items():
        if count >= 3:
            anomalies.append({
                "type": "high_frequency_tool_use",
                "tool": tool,
                "count": count,
                "recommendation": "Check for potential agent loop"
            })
    
    return anomalies
