function setFallbackImage(img) {
  img.onerror = function () {
    img.onerror = null;
    img.src = "/static/images/fallback.svg";
  };
}

function applyFallbackToAllCovers() {
  var covers = document.querySelectorAll("img.book-cover");
  for (var i = 0; i < covers.length; i++) {
    setFallbackImage(covers[i]);
  }
}

function showSummary(summary) {
  var modal = document.getElementById("summaryModal");
  var content = document.getElementById("summaryContent") || document.getElementById("summaryText");
  if (!modal || !content) return;

  if (summary && summary.trim && summary.trim() !== "") {
    content.innerText = summary;
  } else {
    content.innerText = "Summary not available for this book.";
  }

  modal.style.display = "flex";
}

function openSummary(text) {
  // keep old function name used in some pages
  showSummary(text || "");
}

function closeSummary() {
  var modal = document.getElementById("summaryModal");
  if (!modal) return;
  modal.style.display = "none";
}

function setupSummaryButton() {
  var btn = document.getElementById("summaryBtn");
  if (!btn) return;
  btn.addEventListener("click", function () {
    var raw = btn.getAttribute("data-summary") || "";
    var text = raw;
    try {
      text = JSON.parse(raw);
    } catch (e) {
      // keep raw text
    }
    showSummary(text);
  });
}

function setupAccordion() {
  var headers = document.querySelectorAll(".acc-head");
  for (var i = 0; i < headers.length; i++) {
    headers[i].addEventListener("click", function () {
      var item = this.parentElement;
      if (!item) return;
      var open = item.classList.contains("open");

      var all = document.querySelectorAll(".acc-item");
      for (var j = 0; j < all.length; j++) {
        all[j].classList.remove("open");
      }

      if (!open) item.classList.add("open");
    });
  }
}

function setupButtonFeedback() {
  var buttons = document.querySelectorAll("button.btn, a.btn");
  for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", function () {
      this.classList.add("clicked");
      var el = this;
      setTimeout(function () {
        el.classList.remove("clicked");
      }, 220);
    });
  }
}

function chatbotAnswer(q) {
  var text = (q || "").toLowerCase().trim();

  if (text.includes("issue") || text.includes("borrow")) {
    return "Go to Books → open a book → click Issue Book. You can issue only if availability is Yes.";
  }
  if (text.includes("return")) {
    return "Go to Profile → Active Issued Books → click Return. If deadline is crossed, it will show Late Return.";
  }
  if (text.includes("deadline") || text.includes("days") || text.includes("due")) {
    return "Return date is 7 days from issue date by default.";
  }
  if (text.includes("admin")) {
    return "Admin can add/edit/delete books and see analytics in the Admin page.";
  }
  if (text.includes("review")) {
    return "Open any book detail page and add a short 1–2 line review.";
  }

  return "Try: 'How to issue book?', 'Return policy?', 'How many days?', 'How to add review?'";
}

function addChatMessage(type, text) {
  var log = document.getElementById("chatLog");
  if (!log) return;
  var div = document.createElement("div");
  div.className = "msg " + type;
  div.innerText = (type === "user" ? "You: " : "Bot: ") + text;
  log.appendChild(div);
  log.scrollTop = log.scrollHeight;
}

function sendChat() {
  var input = document.getElementById("chatInput");
  if (!input) return;
  var q = input.value;
  if (!q.trim()) return;
  addChatMessage("user", q);
  var ans = chatbotAnswer(q);
  addChatMessage("bot", ans);
  input.value = "";
}

window.addEventListener("DOMContentLoaded", function () {
  applyFallbackToAllCovers();
  setupSummaryButton();
  setupAccordion();
  setupButtonFeedback();

  var chatBtn = document.getElementById("chatSend");
  if (chatBtn) {
    chatBtn.addEventListener("click", sendChat);
  }

  var chatInput = document.getElementById("chatInput");
  if (chatInput) {
    chatInput.addEventListener("keydown", function (e) {
      if (e.key === "Enter") sendChat();
    });
  }

  var closeBtn = document.getElementById("summaryClose");
  if (closeBtn) {
    closeBtn.addEventListener("click", closeSummary);
  }

  var modal = document.getElementById("summaryModal");
  if (modal) {
    modal.addEventListener("click", function (e) {
      if (e.target === modal) closeSummary();
    });
  }
});

