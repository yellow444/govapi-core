"use strict";

const byId = (id) => document.getElementById(id);
const countries = byId("countries");
const workspace = byId("workspace");
const form = byId("demo");
const receipt = byId("receipt");
const feedStatus = byId("feed-status");
const messages = byId("messages");
let active;

async function api(url, options) {
  const response = await fetch(url, options);
  const body = await response.json();
  if (!response.ok) throw new Error(body.error);
  return body;
}

function node(tag, text) {
  const element = document.createElement(tag);
  element.textContent = text;
  return element;
}

async function refreshFeed(profile) {
  messages.replaceChildren();
  feedStatus.textContent = "Loading the feed…";
  try {
    const feed = await api("/api/feed?country=" + encodeURIComponent(profile.id));
    if (active !== profile) return;
    if (!feed) {
      feedStatus.textContent = "The Bell feed is not connected.";
      return;
    }
    feedStatus.textContent = "Demo feed · " + feed.organization;
    messages.replaceChildren(...feed.items.map(item => {
      const row = node("li", "");
      row.append(node("strong", item.subject), node("time", item.received_at));
      return row;
    }));
  } catch (error) {
    if (active === profile) feedStatus.textContent = error.message;
  }
}

function select(profile) {
  active = profile;
  workspace.hidden = false;
  byId("status").hidden = true;
  byId("country").textContent = profile.country;
  byId("platform").textContent = profile.platform;
  byId("summary").textContent = profile.summary;
  receipt.hidden = true;
  for (const button of countries.children) {
    button.setAttribute("aria-pressed", String(button.dataset.country === profile.id));
  }
  byId("steps").replaceChildren(...profile.steps.map(step => {
    const entry = node("li", "");
    const link = node("a", step.source + " ↗");
    link.href = step.url;
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    entry.append(node("h3", step.title), node("p", step.detail), link);
    return entry;
  }));
  byId("fields").replaceChildren(...Object.entries(profile.fields).map(([name, title]) => {
    const label = node("label", title);
    const input = document.createElement("input");
    input.name = name;
    input.required = true;
    input.maxLength = 120;
    input.autocomplete = "off";
    label.append(input);
    return label;
  }));
  byId("bell").hidden = !profile.bell;
  if (profile.bell) void refreshFeed(profile);
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const profile = active;
  const fields = Object.fromEntries(new FormData(form));
  receipt.hidden = false;
  receipt.textContent = "Validating fields…";
  try {
    const value = await api("/api/mock", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ country: profile.id, fields }),
    });
    if (active === profile) receipt.textContent = "Demo receipt · " + value.receipt;
  } catch (error) {
    if (active === profile) receipt.textContent = error.message;
  }
});

byId("refresh").addEventListener("click", () => refreshFeed(active));

api("/api/plugins").then(profiles => {
  if (!profiles.length) {
    byId("status").textContent = "No plugins are connected. Pass a manifest when starting Core.";
    return;
  }
  for (const profile of profiles) {
    const button = node("button", profile.country);
    button.dataset.country = profile.id;
    button.addEventListener("click", () => select(profile));
    countries.append(button);
  }
  select(profiles.find(profile => profile.id === "ru") || profiles[0]);
}).catch(error => {
  byId("status").textContent = "Could not load countries. " + error.message;
});
