/**
 * FetchForm — data-fetch="true" olan formları yakalar, Fetch API ile gönderir.
 * Spinner, Bootstrap Toast bildirimi ve field hata gösterimi dahil.
 *
 * Kullanım:
 *   <form data-fetch="true" action="/api/..." method="post">
 *     <input name="email" type="email">
 *     <button type="submit">Gönder</button>
 *   </form>
 *
 * Opsiyonel data attribute'lar:
 *   data-success-msg="Kaydedildi!"   — özel başarı mesajı
 *   data-clear="false"               — başarı sonrası formu temizleme
 *   data-redirect="/hedef/"          — başarı sonrası yönlendirme
 */
class FetchForm {
  constructor(form) {
    this.form = form;
    form.addEventListener('submit', (e) => this._onSubmit(e));
  }

  async _onSubmit(e) {
    e.preventDefault();
    const btn = this.form.querySelector('[type="submit"]');
    const originalHtml = btn ? btn.innerHTML : null;

    if (btn) {
      btn.disabled = true;
      btn.innerHTML =
        `<span class="spinner-border spinner-border-sm me-1" role="status" aria-hidden="true"></span>${originalHtml}`;
    }
    this._clearErrors();

    try {
      const res = await fetch(this.form.action || window.location.href, {
        method: (this.form.method || 'POST').toUpperCase(),
        body: new FormData(this.form),
        headers: {
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': this._csrfToken(),
        },
      });

      let data = {};
      try { data = await res.json(); } catch { /* boş yanıt */ }

      if (res.ok && data.status !== 'error') {
        const msg = this.form.dataset.successMsg || data.message || 'Başarıyla gönderildi.';
        this._toast(msg, 'success');
        if (this.form.dataset.clear !== 'false') this.form.reset();
        if (this.form.dataset.redirect) window.location.href = this.form.dataset.redirect;
      } else {
        if (data.errors) this._showErrors(data.errors);
        this._toast(data.message || 'Bir hata oluştu.', 'danger');
      }
    } catch {
      this._toast('Bağlantı hatası. Lütfen tekrar deneyin.', 'danger');
    } finally {
      if (btn) { btn.disabled = false; btn.innerHTML = originalHtml; }
    }
  }

  _csrfToken() {
    const input = this.form.querySelector('[name="csrfmiddlewaretoken"]');
    if (input) return input.value;
    const m = document.cookie.match(/csrftoken=([^;]+)/);
    return m ? m[1] : '';
  }

  _showErrors(errors) {
    for (const [field, msgs] of Object.entries(errors)) {
      const el = this.form.querySelector(`[name="${field}"]`);
      if (!el) continue;
      el.classList.add('is-invalid');
      const div = document.createElement('div');
      div.className = 'invalid-feedback d-block fetch-form-error';
      div.textContent = Array.isArray(msgs) ? msgs.join(' ') : msgs;
      el.insertAdjacentElement('afterend', div);
    }
  }

  _clearErrors() {
    this.form.querySelectorAll('.fetch-form-error').forEach((el) => el.remove());
    this.form.querySelectorAll('.is-invalid').forEach((el) => el.classList.remove('is-invalid'));
  }

  _toast(message, type = 'success') {
    let container = document.getElementById('ff-toast-container');
    if (!container) {
      container = document.createElement('div');
      container.id = 'ff-toast-container';
      container.className = 'toast-container position-fixed bottom-0 end-0 p-3';
      container.style.zIndex = '1100';
      document.body.appendChild(container);
    }

    const el = document.createElement('div');
    el.className = `toast align-items-center text-white bg-${type} border-0`;
    el.setAttribute('role', 'alert');
    el.innerHTML = `
      <div class="d-flex">
        <div class="toast-body">${message}</div>
        <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Kapat"></button>
      </div>`;
    container.appendChild(el);

    if (window.bootstrap?.Toast) {
      const t = new bootstrap.Toast(el, { delay: 3500 });
      t.show();
      el.addEventListener('hidden.bs.toast', () => el.remove());
    } else {
      setTimeout(() => el.remove(), 4000);
    }
  }

  static initAll() {
    document.querySelectorAll('form[data-fetch="true"]').forEach((f) => new FetchForm(f));
  }
}

document.addEventListener('DOMContentLoaded', FetchForm.initAll);
