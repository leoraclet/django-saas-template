var Ft = Object.defineProperty;
var Ot = (t, n, e) =>
  n in t
    ? Ft(t, n, { enumerable: !0, configurable: !0, writable: !0, value: e })
    : (t[n] = e);
var Y = (t, n, e) => Ot(t, typeof n != 'symbol' ? n + '' : n, e);
(function () {
  const n = document.createElement('link').relList;
  if (n && n.supports && n.supports('modulepreload')) return;
  for (const a of document.querySelectorAll('link[rel="modulepreload"]')) l(a);
  new MutationObserver((a) => {
    for (const r of a)
      if (r.type === 'childList')
        for (const o of r.addedNodes)
          o.tagName === 'LINK' && o.rel === 'modulepreload' && l(o);
  }).observe(document, { childList: !0, subtree: !0 });
  function e(a) {
    const r = {};
    return (
      a.integrity && (r.integrity = a.integrity),
      a.referrerPolicy && (r.referrerPolicy = a.referrerPolicy),
      a.crossOrigin === 'use-credentials'
        ? (r.credentials = 'include')
        : a.crossOrigin === 'anonymous'
          ? (r.credentials = 'omit')
          : (r.credentials = 'same-origin'),
      r
    );
  }
  function l(a) {
    if (a.ep) return;
    a.ep = !0;
    const r = e(a);
    fetch(a.href, r);
  }
})();
const nt = !1;
var Rt = Array.isArray,
  Mt = Array.prototype.indexOf,
  Dt = Array.from,
  It = Object.defineProperty,
  et = Object.getOwnPropertyDescriptor,
  rt = Object.isExtensible;
const F = 2,
  ct = 4,
  dt = 8,
  Lt = 16,
  M = 32,
  I = 64,
  $ = 128,
  N = 256,
  U = 512,
  w = 1024,
  L = 2048,
  P = 4096,
  V = 8192,
  G = 16384,
  vt = 32768,
  Pt = 65536,
  Bt = 1 << 18,
  qt = 1 << 19,
  lt = 1 << 20,
  ht = new (class extends Error {
    constructor() {
      super(...arguments);
      Y(this, 'name', 'StaleReactionError');
      Y(
        this,
        'message',
        'The reaction that called `getAbortSignal()` was re-run or destroyed',
      );
    }
  })();
function jt(t) {
  return t === this.v;
}
function Ut() {
  throw new Error('https://svelte.dev/e/effect_update_depth_exceeded');
}
let J = !1,
  Vt = !1;
function Ht() {
  J = !0;
}
const zt = 2;
let b = null;
function at(t) {
  b = t;
}
function Wt(t, n = !1, e) {
  var l = (b = {
    p: b,
    c: null,
    d: !1,
    e: null,
    m: !1,
    s: t,
    x: null,
    l: null,
  });
  (J && !n && (b.l = { s: null, u: null, r1: [], r2: Qt(!1) }),
    ln(() => {
      l.d = !0;
    }));
}
function Yt(t) {
  const n = b;
  if (n !== null) {
    const o = n.e;
    if (o !== null) {
      var e = h,
        l = v;
      n.e = null;
      try {
        for (var a = 0; a < o.length; a++) {
          var r = o[a];
          (R(r.effect), O(r.reaction), sn(r.fn));
        }
      } finally {
        (R(e), O(l));
      }
    }
    ((b = n.p), (n.m = !0));
  }
  return {};
}
function Kt() {
  return !J || (b !== null && b.l === null);
}
function pt(t) {
  var n = t.effects;
  if (n !== null) {
    t.effects = null;
    for (var e = 0; e < n.length; e += 1) S(n[e]);
  }
}
function $t(t) {
  for (var n = t.parent; n !== null; ) {
    if ((n.f & F) === 0) return n;
    n = n.parent;
  }
  return null;
}
function Gt(t) {
  var n,
    e = h;
  R($t(t));
  try {
    (pt(t), (n = Tt(t)));
  } finally {
    R(e);
  }
  return n;
}
function Jt(t) {
  var n = Gt(t);
  if ((t.equals(n) || ((t.v = n), (t.wv = hn())), !Z)) {
    var e = (C || (t.f & N) !== 0) && t.deps !== null ? P : w;
    y(t, e);
  }
}
const Zt = new Map();
function Qt(t, n) {
  var e = { f: 0, v: t, reactions: null, equals: jt, rv: 0, wv: 0 };
  return e;
}
var st, _t, bt, gt;
function Xt() {
  if (st === void 0) {
    ((st = window), (_t = /Firefox/.test(navigator.userAgent)));
    var t = Element.prototype,
      n = Node.prototype,
      e = Text.prototype;
    ((bt = et(n, 'firstChild').get),
      (gt = et(n, 'nextSibling').get),
      rt(t) &&
        ((t.__click = void 0),
        (t.__className = void 0),
        (t.__attributes = null),
        (t.__style = void 0),
        (t.__e = void 0)),
      rt(e) && (e.__t = void 0));
  }
}
function tn(t = '') {
  return document.createTextNode(t);
}
function nn(t) {
  return bt.call(t);
}
function en(t) {
  return gt.call(t);
}
function rn(t, n) {
  var e = n.last;
  e === null
    ? (n.last = n.first = t)
    : ((e.next = t), (t.prev = e), (n.last = t));
}
function W(t, n, e, l = !0) {
  var a = h,
    r = {
      ctx: b,
      deps: null,
      nodes_start: null,
      nodes_end: null,
      f: t | L,
      first: null,
      fn: n,
      last: null,
      next: null,
      parent: a,
      b: a && a.b,
      prev: null,
      teardown: null,
      transitions: null,
      wv: 0,
      ac: null,
    };
  if (e)
    try {
      (X(r), (r.f |= vt));
    } catch (d) {
      throw (S(r), d);
    }
  else n !== null && St(r);
  var o =
    e &&
    r.deps === null &&
    r.first === null &&
    r.nodes_start === null &&
    r.teardown === null &&
    (r.f & (qt | $)) === 0;
  if (!o && l && (a !== null && rn(r, a), v !== null && (v.f & F) !== 0)) {
    var u = v;
    (u.effects ?? (u.effects = [])).push(r);
  }
  return r;
}
function ln(t) {
  const n = W(dt, null, !1);
  return (y(n, w), (n.teardown = t), n);
}
function an(t) {
  const n = W(I, t, !0);
  return (e = {}) =>
    new Promise((l) => {
      e.outro
        ? cn(n, () => {
            (S(n), l(void 0));
          })
        : (S(n), l(void 0));
    });
}
function sn(t) {
  return W(ct, t, !1);
}
function on(t, n = !0) {
  return W(dt | M, t, !0, n);
}
function mt(t) {
  var n = t.teardown;
  if (n !== null) {
    const e = Z,
      l = v;
    (ot(!0), O(null));
    try {
      n.call(null);
    } finally {
      (ot(e), O(l));
    }
  }
}
function wt(t, n = !1) {
  var a;
  var e = t.first;
  for (t.first = t.last = null; e !== null; ) {
    (a = e.ac) == null || a.abort(ht);
    var l = e.next;
    ((e.f & I) !== 0 ? (e.parent = null) : S(e, n), (e = l));
  }
}
function un(t) {
  for (var n = t.first; n !== null; ) {
    var e = n.next;
    ((n.f & M) === 0 && S(n), (n = e));
  }
}
function S(t, n = !0) {
  var e = !1;
  ((n || (t.f & Bt) !== 0) &&
    t.nodes_start !== null &&
    t.nodes_end !== null &&
    (fn(t.nodes_start, t.nodes_end), (e = !0)),
    wt(t, n && !e),
    z(t, 0),
    y(t, G));
  var l = t.transitions;
  if (l !== null) for (const r of l) r.stop();
  mt(t);
  var a = t.parent;
  (a !== null && a.first !== null && xt(t),
    (t.next =
      t.prev =
      t.teardown =
      t.ctx =
      t.deps =
      t.fn =
      t.nodes_start =
      t.nodes_end =
      t.ac =
        null));
}
function fn(t, n) {
  for (; t !== null; ) {
    var e = t === n ? null : en(t);
    (t.remove(), (t = e));
  }
}
function xt(t) {
  var n = t.parent,
    e = t.prev,
    l = t.next;
  (e !== null && (e.next = l),
    l !== null && (l.prev = e),
    n !== null &&
      (n.first === t && (n.first = l), n.last === t && (n.last = e)));
}
function cn(t, n) {
  var e = [];
  (yt(t, e, !0),
    dn(e, () => {
      (S(t), n && n());
    }));
}
function dn(t, n) {
  var e = t.length;
  if (e > 0) {
    var l = () => --e || n();
    for (var a of t) a.out(l);
  } else n();
}
function yt(t, n, e) {
  if ((t.f & V) === 0) {
    if (((t.f ^= V), t.transitions !== null))
      for (const o of t.transitions) (o.is_global || e) && n.push(o);
    for (var l = t.first; l !== null; ) {
      var a = l.next,
        r = (l.f & Pt) !== 0 || (l.f & M) !== 0;
      (yt(l, n, r ? e : !1), (l = a));
    }
  }
}
function vn(t) {
  var n = h;
  if ((n.f & vt) === 0) {
    if ((n.f & $) === 0) throw t;
    n.fn(t);
  } else Et(t, n);
}
function Et(t, n) {
  for (; n !== null; ) {
    if ((n.f & $) !== 0)
      try {
        n.b.error(t);
        return;
      } catch {}
    n = n.parent;
  }
  throw t;
}
let K = !1,
  H = null,
  T = !1,
  Z = !1;
function ot(t) {
  Z = t;
}
let j = [];
let v = null,
  D = !1;
function O(t) {
  v = t;
}
let h = null;
function R(t) {
  h = t;
}
let k = null,
  g = null,
  _ = 0,
  m = null,
  kt = 1,
  it = 0,
  C = !1;
function hn() {
  return ++kt;
}
function Q(t) {
  var i;
  var n = t.f;
  if ((n & L) !== 0) return !0;
  if ((n & P) !== 0) {
    var e = t.deps,
      l = (n & N) !== 0;
    if (e !== null) {
      var a,
        r,
        o = (n & U) !== 0,
        u = l && h !== null && !C,
        d = e.length;
      if (o || u) {
        var c = t,
          x = c.parent;
        for (a = 0; a < d; a++)
          ((r = e[a]),
            (o ||
              !(
                (i = r == null ? void 0 : r.reactions) != null && i.includes(c)
              )) &&
              (r.reactions ?? (r.reactions = [])).push(c));
        (o && (c.f ^= U), u && x !== null && (x.f & N) === 0 && (c.f ^= N));
      }
      for (a = 0; a < d; a++)
        if (((r = e[a]), Q(r) && Jt(r), r.wv > t.wv)) return !0;
    }
    (!l || (h !== null && !C)) && y(t, w);
  }
  return !1;
}
function Ct(t, n, e = !0) {
  var l = t.reactions;
  if (l !== null)
    for (var a = 0; a < l.length; a++) {
      var r = l[a];
      (k != null && k[1].includes(t) && k[0] === v) ||
        ((r.f & F) !== 0
          ? Ct(r, n, !1)
          : n === r && (e ? y(r, L) : (r.f & w) !== 0 && y(r, P), St(r)));
    }
}
function Tt(t) {
  var f;
  var n = g,
    e = _,
    l = m,
    a = v,
    r = C,
    o = k,
    u = b,
    d = D,
    c = t.f;
  ((g = null),
    (_ = 0),
    (m = null),
    (C = (c & N) !== 0 && (D || !T || v === null)),
    (v = (c & (M | I)) === 0 ? t : null),
    (k = null),
    at(t.ctx),
    (D = !1),
    it++,
    (t.f |= lt),
    t.ac !== null && (t.ac.abort(ht), (t.ac = null)));
  try {
    var x = (0, t.fn)(),
      i = t.deps;
    if (g !== null) {
      var s;
      if ((z(t, _), i !== null && _ > 0))
        for (i.length = _ + g.length, s = 0; s < g.length; s++) i[_ + s] = g[s];
      else t.deps = i = g;
      if (!C || ((c & F) !== 0 && t.reactions !== null))
        for (s = _; s < i.length; s++)
          ((f = i[s]).reactions ?? (f.reactions = [])).push(t);
    } else i !== null && _ < i.length && (z(t, _), (i.length = _));
    if (Kt() && m !== null && !D && i !== null && (t.f & (F | P | L)) === 0)
      for (s = 0; s < m.length; s++) Ct(m[s], t);
    return (
      a !== null &&
        a !== t &&
        (it++, m !== null && (l === null ? (l = m) : l.push(...m))),
      x
    );
  } catch (p) {
    vn(p);
  } finally {
    ((g = n),
      (_ = e),
      (m = l),
      (v = a),
      (C = r),
      (k = o),
      at(u),
      (D = d),
      (t.f ^= lt));
  }
}
function pn(t, n) {
  let e = n.reactions;
  if (e !== null) {
    var l = Mt.call(e, t);
    if (l !== -1) {
      var a = e.length - 1;
      a === 0 ? (e = n.reactions = null) : ((e[l] = e[a]), e.pop());
    }
  }
  e === null &&
    (n.f & F) !== 0 &&
    (g === null || !g.includes(n)) &&
    (y(n, P), (n.f & (N | U)) === 0 && (n.f ^= U), pt(n), z(n, 0));
}
function z(t, n) {
  var e = t.deps;
  if (e !== null) for (var l = n; l < e.length; l++) pn(t, e[l]);
}
function X(t) {
  var n = t.f;
  if ((n & G) === 0) {
    y(t, w);
    var e = h,
      l = T;
    ((h = t), (T = !0));
    try {
      ((n & Lt) !== 0 ? un(t) : wt(t), mt(t));
      var a = Tt(t);
      ((t.teardown = typeof a == 'function' ? a : null), (t.wv = kt));
      var r;
      nt && Vt && (t.f & L) !== 0 && t.deps;
    } finally {
      ((T = l), (h = e));
    }
  }
}
function _n() {
  try {
    Ut();
  } catch (t) {
    if (H !== null) Et(t, H);
    else throw t;
  }
}
function bn() {
  var t = T;
  try {
    var n = 0;
    for (T = !0; j.length > 0; ) {
      n++ > 1e3 && _n();
      var e = j,
        l = e.length;
      j = [];
      for (var a = 0; a < l; a++) {
        var r = mn(e[a]);
        gn(r);
      }
      Zt.clear();
    }
  } finally {
    ((K = !1), (T = t), (H = null));
  }
}
function gn(t) {
  var n = t.length;
  if (n !== 0)
    for (var e = 0; e < n; e++) {
      var l = t[e];
      (l.f & (G | V)) === 0 &&
        Q(l) &&
        (X(l),
        l.deps === null &&
          l.first === null &&
          l.nodes_start === null &&
          (l.teardown === null ? xt(l) : (l.fn = null)));
    }
}
function St(t) {
  K || ((K = !0), queueMicrotask(bn));
  for (var n = (H = t); n.parent !== null; ) {
    n = n.parent;
    var e = n.f;
    if ((e & (I | M)) !== 0) {
      if ((e & w) === 0) return;
      n.f ^= w;
    }
  }
  j.push(n);
}
function mn(t) {
  for (var n = [], e = t; e !== null; ) {
    var l = e.f,
      a = (l & (M | I)) !== 0,
      r = a && (l & w) !== 0;
    if (!r && (l & V) === 0) {
      (l & ct) !== 0 ? n.push(e) : a ? (e.f ^= w) : Q(e) && X(e);
      var o = e.first;
      if (o !== null) {
        e = o;
        continue;
      }
    }
    var u = e.parent;
    for (e = e.next; e === null && u !== null; ) ((e = u.next), (u = u.parent));
  }
  return n;
}
const wn = -7169;
function y(t, n) {
  t.f = (t.f & wn) | n;
}
const xn = ['touchstart', 'touchmove'];
function yn(t) {
  return xn.includes(t);
}
const En = new Set(),
  ut = new Set();
function q(t) {
  var tt;
  var n = this,
    e = n.ownerDocument,
    l = t.type,
    a = ((tt = t.composedPath) == null ? void 0 : tt.call(t)) || [],
    r = a[0] || t.target,
    o = 0,
    u = t.__root;
  if (u) {
    var d = a.indexOf(u);
    if (d !== -1 && (n === document || n === window)) {
      t.__root = n;
      return;
    }
    var c = a.indexOf(n);
    if (c === -1) return;
    d <= c && (o = d);
  }
  if (((r = a[o] || t.target), r !== n)) {
    It(t, 'currentTarget', {
      configurable: !0,
      get() {
        return r || e;
      },
    });
    var x = v,
      i = h;
    (O(null), R(null));
    try {
      for (var s, f = []; r !== null; ) {
        var p = r.assignedSlot || r.parentNode || r.host || null;
        try {
          var E = r['__' + l];
          if (E != null && (!r.disabled || t.target === r))
            if (Rt(E)) {
              var [At, ...Nt] = E;
              At.apply(r, [t, ...Nt]);
            } else E.call(r, t);
        } catch (B) {
          s ? f.push(B) : (s = B);
        }
        if (t.cancelBubble || p === n || p === null) break;
        r = p;
      }
      if (s) {
        for (let B of f)
          queueMicrotask(() => {
            throw B;
          });
        throw s;
      }
    } finally {
      ((t.__root = n), delete t.currentTarget, O(x), R(i));
    }
  }
}
function kn(t) {
  var n = document.createElement('template');
  return ((n.innerHTML = t.replaceAll('<!>', '<!---->')), n.content);
}
function Cn(t, n) {
  var e = h;
  e.nodes_start === null && ((e.nodes_start = t), (e.nodes_end = n));
}
function Tn(t, n) {
  var e = (n & zt) !== 0,
    l,
    a = !t.startsWith('<!>');
  return () => {
    l === void 0 && (l = kn(a ? t : '<!>' + t));
    var r = e || _t ? document.importNode(l, !0) : l.cloneNode(!0);
    {
      var o = nn(r),
        u = r.lastChild;
      Cn(o, u);
    }
    return r;
  };
}
function Sn(t, n) {
  t !== null && t.before(n);
}
function An(t, n) {
  return Nn(t, n);
}
const A = new Map();
function Nn(
  t,
  { target: n, anchor: e, props: l = {}, events: a, context: r, intro: o = !0 },
) {
  Xt();
  var u = new Set(),
    d = (i) => {
      for (var s = 0; s < i.length; s++) {
        var f = i[s];
        if (!u.has(f)) {
          u.add(f);
          var p = yn(f);
          n.addEventListener(f, q, { passive: p });
          var E = A.get(f);
          E === void 0
            ? (document.addEventListener(f, q, { passive: p }), A.set(f, 1))
            : A.set(f, E + 1);
        }
      }
    };
  (d(Dt(En)), ut.add(d));
  var c = void 0,
    x = an(() => {
      var i = e ?? n.appendChild(tn());
      return (
        on(() => {
          if (r) {
            Wt({});
            var s = b;
            s.c = r;
          }
          (a && (l.$$events = a), (c = t(i, l) || {}), r && Yt());
        }),
        () => {
          var p;
          for (var s of u) {
            n.removeEventListener(s, q);
            var f = A.get(s);
            --f === 0
              ? (document.removeEventListener(s, q), A.delete(s))
              : A.set(s, f);
          }
          (ut.delete(d),
            i !== e && ((p = i.parentNode) == null || p.removeChild(i)));
        }
      );
    });
  return (Fn.set(c, x), c);
}
let Fn = new WeakMap();
const On = '5';
var ft;
typeof window < 'u' &&
  (
    (ft = window.__svelte ?? (window.__svelte = {})).v ?? (ft.v = new Set())
  ).add(On);
Ht();
var Rn = Tn(
  '<div class="navbar bg-base-100 shadow-sm"><div class="navbar-start"><div class="dropdown"><div tabindex="0" role="button" class="btn btn-ghost btn-circle"><svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7"></path></svg></div> <ul tabindex="0" class="menu menu-sm dropdown-content bg-base-100 rounded-box z-1 mt-3 w-52 p-2 shadow"><li><a>Homepage</a></li> <li><a>Portfolio</a></li> <li><a>About</a></li></ul></div></div> <div class="navbar-center"><a class="btn btn-ghost text-xl">daisyUI</a></div> <div class="navbar-end"><button class="btn btn-ghost btn-circle"><svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg></button> <button class="btn btn-ghost btn-circle"><div class="indicator"><svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"></path></svg> <span class="badge badge-xs badge-primary indicator-item"></span></div></button></div></div> <br/> <br/> <button class="btn btn-neutral">Neutral</button> <button class="btn btn-primary">Primary</button> <button class="btn btn-secondary">Secondary</button> <button class="btn btn-accent">Accent</button> <button class="btn btn-info">Info</button> <button class="btn btn-success">Success</button> <button class="btn btn-warning">Warning</button> <button class="btn btn-error">Error</button> <br/> <br/> <div class="overflow-x-auto"><table class="table"><thead><tr><th><label><input type="checkbox" class="checkbox"/></label></th><th>Name</th><th>Job</th><th>Favorite Color</th><th></th></tr></thead><tbody><tr><th><label><input type="checkbox" class="checkbox"/></label></th><td><div class="flex items-center gap-3"><div class="avatar"><div class="mask mask-squircle h-12 w-12"><img src="https://img.daisyui.com/images/profile/demo/2@94.webp" alt="Avatar Tailwind CSS Component"/></div></div> <div><div class="font-bold">Hart Hagerty</div> <div class="text-sm opacity-50">United States</div></div></div></td><td>Zemlak, Daniel and Leannon <br/> <span class="badge badge-ghost badge-sm">Desktop Support Technician</span></td><td>Purple</td><th><button class="btn btn-ghost btn-xs">details</button></th></tr><tr><th><label><input type="checkbox" class="checkbox"/></label></th><td><div class="flex items-center gap-3"><div class="avatar"><div class="mask mask-squircle h-12 w-12"><img src="https://img.daisyui.com/images/profile/demo/3@94.webp" alt="Avatar Tailwind CSS Component"/></div></div> <div><div class="font-bold">Brice Swyre</div> <div class="text-sm opacity-50">China</div></div></div></td><td>Carroll Group <br/> <span class="badge badge-ghost badge-sm">Tax Accountant</span></td><td>Red</td><th><button class="btn btn-ghost btn-xs">details</button></th></tr><tr><th><label><input type="checkbox" class="checkbox"/></label></th><td><div class="flex items-center gap-3"><div class="avatar"><div class="mask mask-squircle h-12 w-12"><img src="https://img.daisyui.com/images/profile/demo/4@94.webp" alt="Avatar Tailwind CSS Component"/></div></div> <div><div class="font-bold">Marjy Ferencz</div> <div class="text-sm opacity-50">Russia</div></div></div></td><td>Rowe-Schoen <br/> <span class="badge badge-ghost badge-sm">Office Assistant I</span></td><td>Crimson</td><th><button class="btn btn-ghost btn-xs">details</button></th></tr><tr><th><label><input type="checkbox" class="checkbox"/></label></th><td><div class="flex items-center gap-3"><div class="avatar"><div class="mask mask-squircle h-12 w-12"><img src="https://img.daisyui.com/images/profile/demo/5@94.webp" alt="Avatar Tailwind CSS Component"/></div></div> <div><div class="font-bold">Yancy Tear</div> <div class="text-sm opacity-50">Brazil</div></div></div></td><td>Wyman-Ledner <br/> <span class="badge badge-ghost badge-sm">Community Outreach Specialist</span></td><td>Indigo</td><th><button class="btn btn-ghost btn-xs">details</button></th></tr></tbody><tfoot><tr><th></th><th>Name</th><th>Job</th><th>Favorite Color</th><th></th></tr></tfoot></table></div> <ul class="menu bg-base-200 lg:menu-horizontal rounded-box"><li><a href="#inbox"><svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"></path></svg> Inbox <span class="badge badge-xs">99+</span></a></li> <li><a href="#updates"><svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg> Updates <span class="badge badge-xs badge-warning">NEW</span></a></li> <li><a href="#stats">Stats <span class="badge badge-xs badge-info"></span></a></li></ul>',
  1,
);
function Mn(t) {
  var n = Rn();
  Sn(t, n);
}
An(Mn, { target: document.getElementById('app') });
