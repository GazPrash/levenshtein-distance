Levenshtein distance, also known as edit distance, is a measure of the similarity between two strings by calculating the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into the other. It is named after the Soviet mathematician Vladimir Levenshtein, who introduced the concept in 1965.

The Levenshtein distance between two strings is often denoted as $lev(a,b)$, where `a` and `b` are the input strings. The goal is to find the minimum number of operations needed to transform string a into string `b`.

$$
\operatorname{lev}(a, b)= \begin{cases}|a| & \text { if }|b|=0, \\ |b| & \text { if }|a|=0, \\ \operatorname{lev}(\operatorname{tail}(a), \operatorname{tail}(b)) & \text { if } \operatorname{head}(a)=\operatorname{head}(b), \\ 1+\min \begin{cases}\operatorname{lev}(\operatorname{tail}(a), b) \\ \operatorname{lev}(a, \operatorname{tail}(b)) \\ \operatorname{lev}(\operatorname{tail}(a), \operatorname{tail}(b))\end{cases} & \text { otherwise }\end{cases}
$$

where the tail of some string $x$ is a string of all but the first character of $x$, and head $(x)$ is the first character of $x$. Either the notation.

Note that the first element in the minimum corresponds to deletion (from $a$ to $b$ ), the second to insertion and the third to replacement.
This definition corresponds directly to the naive recursive implementation.
