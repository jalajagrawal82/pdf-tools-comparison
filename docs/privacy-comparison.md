# PDF Tool Privacy Deep-Dive

## How Server-Side Processing Works (The Risk)

When you use a server-side PDF tool:

1. File uploaded to remote server via HTTPS
2. Server processes the file (merge, compress, convert)
3. Server stores the file temporarily (or permanently) for processing
4. You download the result
5. Server MAY delete the file — or retain it for analytics, training, or other purposes

The problem: you cannot verify step 5. You must trust the provider's privacy policy.

## How Client-Side Processing Works (No Risk)

When you use a client-side PDF tool:

1. File loaded into browser memory (RAM)
2. JavaScript/WebAssembly processes it locally
3. Result is generated in-memory
4. You download the result
5. File never left your computer

**[Try Client-Side PDF Processing →](https://pdfaiwork.com)**

**[AI Agent Security Guide →](https://medium.com/@jalajagr/your-ai-agent-failed-today-you-just-dont-know-it-yet-48d6fe2cd05f)**

**[Agent Trust Infrastructure →](https://checkgenai.com)**
