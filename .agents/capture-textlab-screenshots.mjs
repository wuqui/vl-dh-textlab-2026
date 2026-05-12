import { createRequire } from "node:module";
import path from "node:path";
import { fileURLToPath } from "node:url";

const require = createRequire(
  "/Users/quirin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.js",
);
const { chromium } = require("playwright");

const user = process.env.TEXTLAB_USER;
const password = process.env.TEXTLAB_PASSWORD;

if (!user || !password) {
  throw new Error("Set TEXTLAB_USER and TEXTLAB_PASSWORD.");
}

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const outDir = path.join(root, "assets/screenshots/textlab/live-deployed-2026-05-11");
const baseUrl = "https://www.wuerschinger.org/textlab/";

const browser = await chromium.launch({ channel: "chrome", headless: true });
const page = await browser.newPage({
  viewport: { width: 1440, height: 980 },
  deviceScaleFactor: 2,
});

async function maybeLogin() {
  await page.goto(baseUrl, { waitUntil: "networkidle" });
  if (await page.getByText(user, { exact: true }).count()) return;

  const email = page.getByRole("textbox", { name: /email|user|username/i });
  const passwordBox = page.getByRole("textbox", { name: /password/i });
  if (await email.count()) {
    await email.first().fill(user);
  } else {
    await page.locator('input[type="email"], input[name*="user"], input[name*="email"]').first().fill(user);
  }
  if (await passwordBox.count()) {
    await passwordBox.first().fill(password);
  } else {
    await page.locator('input[type="password"]').first().fill(password);
  }
  await page.getByRole("button", { name: /log in|login|sign in|anmelden/i }).first().click();
  await page.waitForLoadState("networkidle");
  await page.getByText(user, { exact: true }).waitFor({ timeout: 15000 });
}

async function screenshot(name, selector = "main") {
  const target = page.locator(selector).first();
  await target.screenshot({ path: path.join(outDir, name) });
}

async function selectCorpus(label) {
  await page.getByRole("combobox", { name: "Corpus selector" }).selectOption({ label });
}

async function runSimple(corpus, term) {
  await selectCorpus(corpus);
  await page.getByRole("button", { name: "Simple Search" }).click();
  await page.getByRole("textbox", { name: "Search" }).fill(term);
  await page.getByRole("button", { name: "Run query" }).click();
  await page.getByText(/Showing hits 1-10|Showing hits/).waitFor({ timeout: 60000 });
}

async function runQueryBuilder() {
  await selectCorpus("DTA (238.3M tokens)");
  await page.getByRole("button", { name: "Query Builder" }).click();
  await page.getByLabel("Token 1 condition 1 attribute").selectOption({ label: "lemma" });
  await page.getByLabel("Token 1 condition 1 value").fill("Demokratie");
  await page.getByRole("textbox", { name: "BCQL Query" }).fill('[lemma="Demokratie"]');
  await screenshot("live-deployed-query-builder-sharp.png");
  await page.getByRole("button", { name: "Run query" }).click();
  await page.getByText("Showing hits 1-10 of 2486.").waitFor({ timeout: 60000 });
}

async function saveResultTab(tabName, fileName, beforeSave) {
  await page.getByRole("tab", { name: tabName }).click();
  if (beforeSave) await beforeSave();
  await screenshot(fileName);
}

await maybeLogin();

await runQueryBuilder();
await screenshot("live-deployed-kwic-demokratie-sharp.png");

await saveResultTab("Frequencies", "live-deployed-frequency-demokratie-sharp.png", async () => {
  const selects = page.locator("select");
  await selects.nth(3).selectOption({ label: "Bucket label" });
  await selects.nth(4).selectOption({ label: "Ascending" });
  await page.getByRole("button", { name: "Run" }).click();
  await page.getByText(/metadata:year|total hits 2\.486/).waitFor({ timeout: 60000 });
});

await saveResultTab("Collocations", "live-deployed-collocations-demokratie-sharp.png", async () => {
  const button = page.getByRole("button", { name: "Run collocations" });
  await button.click();
  await page.getByText("Analyzed hits").waitFor({ timeout: 60000 });
});

await saveResultTab("Semantic Space", "live-deployed-semantic-space-demokratie-sharp.png", async () => {
  const button = page.getByRole("button", { name: /Analyze|Re-analyze/ });
  await button.click();
  await page.getByText("Points").waitFor({ timeout: 90000 });
});

await saveResultTab("Topics", "live-deployed-topics-demokratie-sharp.png", async () => {
  const button = page.getByRole("button", { name: "Run topic modeling" });
  await button.click();
  await page.getByText("Status:").waitFor({ timeout: 120000 });
  await page.getByText("Selected topic terms").waitFor({ timeout: 120000 });
});

await page.getByRole("button", { name: "Edit" }).click();
await page.getByRole("button", { name: "Semantic Search" }).click();
await page
  .getByRole("textbox", { name: "Question" })
  .fill("Wie wird das Verhältnis von Mensch und Maschine im 19. Jahrhundert beschrieben?");
await page.getByRole("button", { name: "Run semantic search" }).click();
await page.getByText("Semantic search backend:").waitFor({ timeout: 90000 });
await screenshot("live-deployed-semantic-search-sharp.png");

await runSimple("English Reddit (41.3M tokens)", "London");
await screenshot("live-deployed-kwic-reddit-london-sharp.png");

await browser.close();
