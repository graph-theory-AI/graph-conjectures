#!/usr/bin/env python3
"""Import literature resolutions and reviewed AI write-ups.

Literature resolutions and model-generated arguments remain separate: only
the former receive the ordinary ``solved`` / ``disproved`` statuses.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REPOSITORY_URL = "https://github.com/graph-theory-AI/Graph-Theory-LLM-Proofs"

DISPROVED_IDS = {
    "1407.5833__00", "1806.00825__01", "1905.12142__00",
    "2201.08204__01", "2208.06629__00", "2410.16495__00",
    "2510.11311__04",
}

# Full-problem Astra referee verdicts whose result was already in the
# literature.  2402.10782__01 is deliberately absent: prior art covers only
# one half of that two-part problem.
ASTRA_ALREADY_KNOWN_IDS = {
    "2510.11311__04",
    "2603.02786__01",
    "2603.02786__04",
    "finding_k_edge_outerplanar_graph_embeddings",
    "imbalance_conjecture",
    "three_chromatic_0_2_graphs",
}

RESOLUTION_ARTICLES = {
    "0911.0885__00": ("Three-coloring triangle-free graphs on surfaces V. Coloring planar graphs with distant anomalies", "https://arxiv.org/abs/0911.0885"),
    "1302.2158__00": ("3 List Coloring Graphs of Girth at least Five on Surfaces", "https://arxiv.org/abs/1710.06898"),
    "1407.5833__00": ("Identifying codes in hereditary classes of graphs and VC-dimension", "https://arxiv.org/abs/1407.5833"),
    "1709.09050__03": ("Topological directions in Cops and Robbers", "https://arxiv.org/abs/1709.09050"),
    "1710.06282__01": ("A tight Erdős–Pósa function for planar minors", "https://arxiv.org/abs/1807.04969"),
    "1802.03727__01": ("Dense induced bipartite subgraphs in triangle-free graphs", "https://arxiv.org/abs/1810.12144"),
    "1802.03727__03": ("Dense induced bipartite subgraphs in triangle-free graphs", "https://arxiv.org/abs/1810.12144"),
    "1802.04179__01": ("Planar graphs without cycles of length 4 or 5 are (7m:2m)-DP-colorable", "https://arxiv.org/abs/2511.12914"),
    "1806.00825__01": ("Short rainbow cycles in graphs and matroids", "https://arxiv.org/abs/1806.00825"),
    "1806.09726__02": ("Bounds on Ramsey Games via Alterations", "https://arxiv.org/abs/1909.02691"),
    "1905.12142__00": ("Combinatorial anti-concentration inequalities, with applications", "https://arxiv.org/abs/1905.12142"),
    "1912.11246__02": ("Graphs with polynomially many minimal separators", "https://arxiv.org/abs/2005.05042"),
    "2001.01607__00": ("Induced subgraphs and tree decompositions XI. Local structure in even-hole-free graphs of large treewidth", "https://arxiv.org/abs/2309.04390"),
    "2006.09269__00": ("Recolouring planar graphs of girth at least five", "https://arxiv.org/abs/2112.00631"),
    "2103.17094__00": ("Weak Coloring Numbers of Intersection Graphs", "https://arxiv.org/abs/2103.17094"),
    "2105.07370__00": ("Strengthening Rödl's theorem", "https://arxiv.org/abs/2105.07370"),
    "2201.08204__01": ("Digraphs with all induced directed cycles of the same length are not dichromatically bounded", "https://arxiv.org/abs/2203.15575"),
    "2208.06629__00": ("Perfect shuffling with fewer lazy transpositions", "https://arxiv.org/abs/2208.06629"),
    "2208.06630__01": ("Short reachability networks", "https://arxiv.org/abs/2208.06630"),
    "2212.02737__00": ("Induced subgraphs and tree decompositions XIII. Basic obstructions in H-free graphs for finite H", "https://arxiv.org/abs/2311.05066"),
    "2401.06062__00": ("On prime Cayley graphs", "https://arxiv.org/abs/2401.06062"),
    "2401.06062__01": ("On prime Cayley graphs", "https://arxiv.org/abs/2401.06062"),
    "2401.06062__02": ("On prime Cayley graphs", "https://arxiv.org/abs/2401.06062"),
    "2410.13008__01": ("When all directed cycles have the same weight", "https://arxiv.org/abs/2601.12746"),
    "2410.16495__00": ("Every Graph is Essential to Large Treewidth", "https://arxiv.org/abs/2502.14775"),
    "1701.03366__00": ("Additive bases and flows in graphs", "https://arxiv.org/abs/1701.03366"),
    "2510.11311__04": ("Avoidability of Digraphs with Height Functions and Orientations of $C_4$", "https://arxiv.org/abs/2609.14368"),
    "2603.02786__01": ("Asymptotically optimal packings of arithmetic progressions with prime differences", "https://arxiv.org/abs/2609.07487"),
    "2603.02786__04": ("Solution to a conjecture of Alon, Dębski, Grytczuk and Przybyło on fixed-cardinality arithmetic progressions", "https://arxiv.org/abs/2607.06113"),
    "finding_k_edge_outerplanar_graph_embeddings": ("Minimum Edge-Outerplanar Embeddings are Polynomial-Time Computable", "https://arxiv.org/abs/2607.08110"),
    "imbalance_conjecture": ("A Proof of the Imbalance Conjecture", "https://arxiv.org/abs/2608.09191"),
    "three_chromatic_0_2_graphs": ("Finite Three-Colourable (0,2)-Graphs Are Bipartite", "https://arxiv.org/abs/2607.10125"),
}

RESOLUTION_METADATA = {
    "1701.03366__00": {
        "article_authors": "Louis Esperet, Rémi de Joannis de Verclos, Tien-Nam Le, Stéphan Thomassé",
        "article_year": 2018,
        "article_venue": "SIAM Journal on Discrete Mathematics 32(1), 534–542",
        "article_arxiv_id": "1701.03366",
        "article_doi": "10.1137/17M1113758",
        "one_line": "Corollary 13(iv) of the source paper proves that every directed 12-edge-connected graph has a $\\mathbb{Z}_5$-antisymmetric flow, directly establishing the requested constant.",
    },
    "2510.11311__04": {
        "article_authors": "Hui Lei, Xiaoyi Wang, Zhijun Xu, Zhenyu Yang",
        "article_year": 2026,
        "article_venue": "arXiv preprint",
        "article_arxiv_id": "2609.14368",
        "one_line": "Lei, Wang, Xu, and Yang classify the Eulerian-avoidability of all orientations of $C_4$ and prove that the one-directed $K_{2,2}$ is not Eulerian-avoidable; hence not every orientation of $C_4$ is Eulerian-avoidable.",
    },
    "2603.02786__01": {
        "article_authors": "Jianfeng Hou, Siyue Liu, Hongbin Zhao",
        "article_year": 2026,
        "article_venue": "arXiv preprint",
        "article_arxiv_id": "2609.07487",
        "one_line": "Hou, Liu, and Zhao prove $M_{\\mathbb{P}(n)}(n)=(\\frac16+o(1))n^3/\\ln n$, settling Conjecture 4 with its predicted constant.",
    },
    "2603.02786__04": {
        "article_authors": "Yaping Mao, Zhao Wang, Meiqin Wei, Gang Yang",
        "article_year": 2026,
        "article_venue": "arXiv preprint",
        "article_arxiv_id": "2607.06113",
        "one_line": "Mao, Wang, Wei, and Yang prove $M_k(n)=(1+o(1))nk$ for every fixed $n$, confirming Conjecture 7.",
    },
    "finding_k_edge_outerplanar_graph_embeddings": {
        "article_authors": "Hantao Yu",
        "article_year": 2026,
        "article_venue": "arXiv preprint",
        "article_arxiv_id": "2607.08110",
        "one_line": "Yu proves that the minimum edge-outerplanarity of a planar graph can be computed in polynomial time, answering Bentz's question affirmatively.",
    },
    "imbalance_conjecture": {
        "article_authors": "James Alexander Schreib, Yousof Yavari",
        "article_year": 2026,
        "article_venue": "arXiv preprint",
        "article_arxiv_id": "2608.09191",
        "one_line": "Schreib and Yavari prove that the positive imbalance multiset $M_G$ is graphic, establishing the imbalance conjecture in full.",
    },
    "three_chromatic_0_2_graphs": {
        "article_authors": "Christopher Williamson",
        "article_year": 2026,
        "article_venue": "arXiv preprint",
        "article_arxiv_id": "2607.10125",
        "one_line": "Williamson proves that every finite three-colourable $(0,2)$-graph is bipartite; consequently no finite $(0,2)$-graph has chromatic number exactly three.",
    },
}


def _known_result(review_id: str, attack: dict, audit_url: str) -> dict:
    article_title, article_url = RESOLUTION_ARTICLES[review_id]
    metadata = RESOLUTION_METADATA.get(review_id, {})
    result = {
        "id": review_id,
        "site_status": "disproved" if review_id in DISPROVED_IDS else "solved",
        "confidence": attack.get("confidence", "unknown"),
        "one_line": metadata.get("one_line", attack.get("one_line", "")),
        "caveats": metadata.get("caveats", "") if metadata else attack.get("caveats", ""),
        "model": attack.get("model", ""),
        "assessed_at": attack.get("when", ""),
        "article_title": article_title,
        "article_url": article_url,
        "audit_url": audit_url,
    }
    result.update({k: v for k, v in metadata.items() if k.startswith("article_")})
    return result


def _pdf_target_id(pdf_path: Path) -> str:
    match = re.match(r"^(\d+\.\d+__\d+|.+?)__", pdf_path.name)
    if not match:
        raise ValueError(f"cannot determine catalog id from PDF name: {pdf_path.name}")
    return match.group(1)


def collect_ai_writeups(source_dir: Path) -> list[dict]:
    """Collect README-listed PDF artifacts with a confirmed referee verdict."""
    readme = (source_dir / "README.md").read_text(encoding="utf-8")
    readme_pdf_paths = sorted(set(re.findall(
        r"\((to_review(?:_astra)?/[^)]+\.pdf)\)",
        readme,
    )))
    if not readme_pdf_paths:
        raise ValueError("no reviewed PDF links found in source README")

    campaigns = {
        "to_review": ("verification/verdicts.json", "initial"),
        "to_review_astra": (
            "verification_astra/verdicts.json",
            "astra",
        ),
    }
    verdicts_by_campaign = {
        pdf_dir_name: {
            item["id"]: item
            for item in json.loads(
                (source_dir / verdicts_name).read_text(encoding="utf-8")
            ).get("verdicts", [])
        }
        for pdf_dir_name, (verdicts_name, _) in campaigns.items()
    }

    writeups = []
    for relative_pdf_path in readme_pdf_paths:
        pdf_path = source_dir / relative_pdf_path
        if not pdf_path.is_file():
            raise FileNotFoundError(f"README-linked PDF not found: {pdf_path}")
        pdf_dir_name = pdf_path.parent.name
        if pdf_dir_name not in campaigns:
            raise ValueError(f"unsupported README PDF directory: {pdf_dir_name}")
        _, campaign = campaigns[pdf_dir_name]
        review_id = _pdf_target_id(pdf_path)
        verdicts = verdicts_by_campaign[pdf_dir_name]
        if review_id not in verdicts:
            raise ValueError(f"no referee verdict for {pdf_path}")
        referee = verdicts[review_id]
        if referee.get("review_verdict") != "CONFIRMED":
            continue
        claimed_verdict = referee.get("claimed_verdict")
        if claimed_verdict not in {"proved", "disproved"}:
            raise ValueError(
                f"PDF {pdf_path.name} has unsupported verdict {claimed_verdict!r}"
            )
        leg = referee.get("leg", "attacks")
        attack = json.loads(
            (source_dir / leg / review_id / "verdict.json").read_text(encoding="utf-8")
        )
        writeups.append({
            "id": review_id,
            "site_status": f"ai-{claimed_verdict}",
            "promote_status": True,
            "claimed_verdict": claimed_verdict,
            "review_verdict": "CONFIRMED",
            "confidence": referee.get("confidence", "unknown"),
            "one_line": referee.get("claimed_one_line") or attack.get("one_line", ""),
            "model": attack.get("model", ""),
            "assessed_at": attack.get("when", ""),
            "campaign": campaign,
            "pdf_url": f"{REPOSITORY_URL}/blob/main/{relative_pdf_path}",
        })

    writeups.sort(key=lambda result: result["id"])
    ids = [result["id"] for result in writeups]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate AI-writeup ids")
    return writeups


def collect_known_resolutions(source_dir: Path) -> dict:
    attacks_dir = source_dir / "attacks"
    if not attacks_dir.is_dir():
        raise FileNotFoundError(f"attack directory not found: {attacks_dir}")
    results = []
    for verdict_path in sorted(attacks_dir.glob("*/verdict.json")):
        attack = json.loads(verdict_path.read_text(encoding="utf-8"))
        review_id = attack.get("id") or verdict_path.parent.name
        if attack.get("verdict") != "already_resolved":
            continue
        if review_id != verdict_path.parent.name:
            raise ValueError(
                f"verdict id {review_id!r} does not match {verdict_path.parent.name!r}"
            )
        results.append(_known_result(
            review_id,
            attack,
            f"{REPOSITORY_URL}/tree/main/attacks/{review_id}",
        ))

    astra_id = "1701.03366__00"
    astra_verdict_path = source_dir / "attacks_arxiv_astra" / astra_id / "verdict.json"
    attack = json.loads(astra_verdict_path.read_text(encoding="utf-8"))
    if attack.get("verdict") != "already_resolved":
        raise ValueError(f"expected {astra_id} to be already_resolved")
    results.append(_known_result(
        astra_id,
        attack,
        f"{REPOSITORY_URL}/tree/main/attacks_arxiv_astra/{astra_id}",
    ))

    referee_doc = json.loads(
        (source_dir / "verification_astra" / "verdicts.json").read_text(encoding="utf-8")
    )
    referee_by_id = {
        item["id"]: item for item in referee_doc.get("verdicts", [])
        if item.get("review_verdict") == "ALREADY_KNOWN"
    }
    missing = ASTRA_ALREADY_KNOWN_IDS - set(referee_by_id)
    if missing:
        raise ValueError(f"missing Astra ALREADY_KNOWN verdicts: {sorted(missing)}")
    for review_id in sorted(ASTRA_ALREADY_KNOWN_IDS):
        referee = referee_by_id[review_id]
        attack = json.loads(
            (source_dir / referee["leg"] / review_id / "verdict.json").read_text(
                encoding="utf-8"
            )
        )
        results.append(_known_result(
            review_id,
            attack,
            f"{REPOSITORY_URL}/blob/main/verification_astra/{review_id}.md",
        ))

    results.sort(key=lambda result: result["id"])
    result_ids = [result["id"] for result in results]
    if len(result_ids) != len(set(result_ids)):
        raise ValueError("duplicate known-resolution ids")

    return {
        "schema_version": 3,
        "source_repository": REPOSITORY_URL,
        "disclaimer": (
            "These status corrections report results attributed to existing papers "
            "or to the final source version. Graph-Theory-LLM-Proofs located and "
            "checked the implication; it is not credited as the author of the result."
        ),
        "results": results,
        "ai_results": collect_ai_writeups(source_dir),
    }


def main() -> int:
    project = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path,
                        default=project.parent / "Graph-Theory-LLM-Proofs")
    parser.add_argument("--output", type=Path,
                        default=project / "data" / "llm_proof_results.json")
    args = parser.parse_args()
    payload = collect_known_resolutions(args.source_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        f"wrote {len(payload['results'])} known resolution(s) and "
        f"{len(payload['ai_results'])} AI write-up(s) to {args.output}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
