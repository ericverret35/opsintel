layout: default
title: Devenir sponsor
permalink: /sponsor/
<h2>Become a sponsor</h2> <p>OpsIntel: veille sécu/devops (CVEs, K8s, GitHub trending, jobs...).</p> <p> <a href="{{<p>Questions : {{ site.contact_email }}</p>
<h2>Devenir sponsor</h2> <p>OpsIntel: veille sécu/devops (CVEs, K8s, GitHub trending, jobs…).</p><p><strong>Offre</strong> : encart site + mention hebdo (à partir de 100 CAD/semaine).</p><p> <a href="{{ site.stripe_payment_link }}" target="_blank" rel="noopener" style="display:inline-block;background:#0a66ff;color:#fff;padding:.6rem 1rem;border-radius:6px;text-decoration:none;font-weight:600;"> Sponsoriser via Stripe </a> </p><p>Questions : {{ site.contact_email }}</p>
Étape 3 — Bandeau “Sponsoriser” visible partout
Tu as déjà le bloc dans _layouts/default.html. Assure-toi qu’il est bien juste après <body> (c’est déjà corrigé chez toi). Si tu veux le bouton aussi sur la home et que index.html n’utilise pas le layout, ajoute ce bloc juste après <body> dans index.html et Commit:

<div style="margin:1rem 0;text-align:center;"> <a href="{{ site.stripe_payment_link }}" target="_blank" rel="noopener" style="display:inline-block;background:#0a66ff;color:#fff;padding:.6rem 1rem;border-radius:6px;text-decoration:none;font-weight:600;"> Sponsoriser via Stripe </a> <span style="margin-left:.75rem;"><a href="/sponsor/">Infos</a></span> </div>
