import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import OpenAI from "openai";

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

if (!process.env.OPENAI_API_KEY) {
  console.error("❌ Chýba OPENAI_API_KEY v .env");
  process.exit(1);
}

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

app.use(cors());
app.use(express.json({ limit: "10mb" }));

// Test endpoint
app.get("/", (req, res) => {
  res.json({
    ok: true,
    name: "Nexa AI Backend",
    status: "online"
  });
});

// AI chat endpoint
app.post("/api/chat", async (req, res) => {
  try {
    const { messages } = req.body;

    if (!Array.isArray(messages) || messages.length === 0) {
      return res.status(400).json({
        error: "Neboli odoslané žiadne správy."
      });
    }

    const response = await openai.responses.create({
      model: "gpt-5",
      instructions:
        "Si Nexa AI, inteligentný AI asistent. Odpovedaj po slovensky, pokiaľ používateľ nepoužije iný jazyk. Buď užitočný, presný a stručný.",
      input: messages.map((message) => ({
        role: message.role,
        content: message.content
      }))
    });

    res.json({
      ok: true,
      reply: response.output_text
    });

  } catch (error) {
    console.error("❌ OpenAI chyba:", error);

    res.status(500).json({
      ok: false,
      error: "Nepodarilo sa získať odpoveď AI."
    });
  }
});

app.listen(PORT, () => {
  console.log(`🚀 Nexa AI backend beží na porte ${PORT}`);
});
