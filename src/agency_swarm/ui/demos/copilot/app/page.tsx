"use client";

import { CopilotKit } from "@copilotkit/react-core";
import { CopilotChat } from "@copilotkit/react-ui";
import "@copilotkit/react-ui/styles.css";

export default function Home() {
  return (
    <CopilotKit runtimeUrl="/api/copilotkit">
      <div className="h-screen w-screen">
        <CopilotChat
          instructions="You are a helpful AI assistant powered by Agency Swarm."
          labels={{
            title: "800x Swarm",
            initial: "Hello! I'm your AI assistant. How can I help you today?",
          }}
        />
      </div>
    </CopilotKit>
  );
}
