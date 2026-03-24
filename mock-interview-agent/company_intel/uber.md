# Uber — LeetCode Interview Intelligence

> Last updated: 2026-03-24
> Sources: LeetCode Discuss, InterviewSolver, Verve Copilot, Glassdoor

---

## Interview Format (Code Screen)

- **Online Assessment (OA):** 3 problems — one Easy/Medium, one Medium, one Hard/contest-style. Runnable code required.
- **Technical Phone Screen / Onsite Coding:** 1–2 problems per round, ~45 min each. Expect follow-ups on time/space complexity.
- **Default language accepted:** Python, Java, C++

---

## Difficulty Distribution

| Difficulty | Share |
|------------|-------|
| Easy       | ~7%   |
| Medium     | ~73%  |
| Hard       | ~20%  |

---

## Top Frequently Asked Problems

Ranked by reported frequency across LeetCode Discuss, Glassdoor, and interview prep aggregators.

| # | LeetCode # | Title | Difficulty | Frequency | Key Topics |
|---|-----------|-------|-----------|-----------|-----------|
| 1 | #3316 | Maximize Amount After Two Days of Conversions | Medium | ★★★★★ | Array, String, Graph |
| 2 | #815  | Bus Routes | Hard | ★★★★★ | BFS, Hash Table |
| 3 | #269  | Alien Dictionary | Hard | ★★★★☆ | Topological Sort, Graph, DFS |
| 4 | #305  | Number of Islands II | Hard | ★★★★☆ | Union-Find, BFS |
| 5 | #362  | Design Hit Counter | Medium | ★★★★☆ | Queue, Binary Search, Design |
| 6 | #200  | Number of Islands | Medium | ★★★★☆ | DFS, BFS, Union-Find |
| 7 | #54   | Spiral Matrix | Medium | ★★★☆☆ | Array, Matrix, Simulation |
| 8 | #79   | Word Search | Medium | ★★★☆☆ | Backtracking, DFS |
| 9 | #146  | LRU Cache | Medium | ★★★☆☆ | Hash Map, Doubly Linked List, Design |
| 10 | #347 | Top K Frequent Elements | Medium | ★★★☆☆ | Heap, Hash Table, Bucket Sort |
| 11 | #399 | Evaluate Division | Medium | ★★★☆☆ | Graph, BFS, Union-Find |
| 12 | #427 | Construct Quad Tree | Medium | ★★★☆☆ | Divide & Conquer, Tree |
| 13 | #528 | Random Pick with Weight | Medium | ★★★☆☆ | Prefix Sum, Binary Search, Randomization |
| 14 | #977 | Squares of a Sorted Array | Easy | ★★★☆☆ | Array, Two Pointers |
| 15 | #1438 | Longest Continuous Subarray With Absolute Diff ≤ Limit | Medium | ★★★☆☆ | Sliding Window, Monotonic Deque |
| 16 | #1   | Two Sum | Easy | ★★★☆☆ | Array, Hash Table |
| 17 | #56  | Merge Intervals | Medium | ★★★☆☆ | Array, Sorting |
| 18 | #230 | Kth Smallest Element in a BST | Medium | ★★★☆☆ | BST, DFS, In-order |
| 19 | #238 | Product of Array Except Self | Medium | ★★★☆☆ | Array, Prefix Sum |
| 20 | #11  | Container With Most Water | Medium | ★★★☆☆ | Array, Two Pointers, Greedy |
| 21 | #3   | Longest Substring Without Repeating Characters | Medium | ★★★☆☆ | Sliding Window, Hash Map |
| 22 | #297 | Serialize and Deserialize Binary Tree | Hard | ★★★☆☆ | Tree, DFS, BFS, Design |
| 23 | #295 | Find Median from Data Stream | Hard | ★★★☆☆ | Two Heaps, Design |
| 24 | #253 | Meeting Rooms II | Medium | ★★★☆☆ | Greedy, Min-Heap, Sorting |
| 25 | #133 | Clone Graph | Medium | ★★★☆☆ | Graph, BFS, DFS, Hash Map |
| 26 | #207 | Course Schedule | Medium | ★★★☆☆ | Topological Sort, DFS, Cycle Detection |
| 27 | #227 | Basic Calculator II | Medium | ★★★☆☆ | Stack, String Parsing |

---

## High-Frequency Topic Areas

1. **Graph traversal** — BFS and DFS come up constantly. Uber products (maps, routing, ride matching) make graph problems a natural fit.
2. **Design problems** — LRU Cache, Hit Counter, TinyURL. Uber loves testing system intuition in coding rounds.
3. **Sliding window / two pointers** — Arrays with constraints on subarrays.
4. **Union-Find** — Islands variants, connected components.
5. **Topological sort** — Alien Dictionary, Course Schedule.
6. **Heap / priority queue** — Top K, Median, Meeting Rooms.

---

## System Design Topics (Onsite)

Uber commonly asks candidates to design:
- **Ride-Sharing Service** (Uber itself — surge pricing, driver matching, ETA)
- **Google Maps / Navigation System** (routing, real-time updates)
- **Design TinyURL** (URL shortener with scale)
- Rate limiter, notification service, or real-time location tracking system

---

## Behavioral Themes

Uber's culture centers around **ownership** and **moving fast**. Common themes:
- Driving a project end-to-end under ambiguity
- Handling a production incident or on-call situation
- Disagreeing with a decision and how you navigated it
- Cross-functional collaboration (eng ↔ PM ↔ data)

---

## Preparation Tips

- Practice **runnable code** — Uber OA requires code that compiles and runs, not pseudocode.
- For graph problems, be ready to switch between **BFS ↔ Dijkstra** (a common follow-up: "what if edges have weights?").
- **Design Hit Counter** is almost a gimme — know the queue + binary search approach and the follow-up (distributed/at-scale version).
- **Alien Dictionary** is a favorite hard problem — practice topological sort from scratch.
- Expect the interviewer to ask for **both time and space complexity** and then push for an optimization.

---

## Sources

- [LeetCode Uber Company Page](https://leetcode.com/company/uber/)
- [Top 30 Uber LeetCode Questions — Verve Copilot](https://www.vervecopilot.com/hot-blogs/uber-leetcode-interview-questions)
- [Uber LeetCode Interview Questions — InterviewSolver](https://interviewsolver.com/interview-questions/uber)
- [Uber L4 Interview Experience (US, Offer) — LeetCode Discuss](https://leetcode.com/discuss/interview-experience/7217970/)
- [Uber SDE-2 Interview 2026 — LeetCode Discuss](https://leetcode.com/discuss/post/7640134/uber-sde-ii-l4-interview-2026-pending-re-or65/)
- [Uber Software Engineer I — Glassdoor](https://www.glassdoor.com/Interview/Uber-Software-Engineer-I-Interview-Questions-EI_IE575263.0,4_KO5,24.htm)
