(ns bird-watcher)

(def last-week
  [0 2 5 3 7 8 4])

(defn today [birds]
  (last birds))

(defn inc-bird [birds]
  (update birds (dec (count birds)) inc))

(defn day-without-birds? [birds]
  (some? (some #(= 0 %) birds)))

(defn n-days-count [birds n]
  (reduce + (subvec birds 0 n)))

(defn busy-days [birds]
  (count (filter #(<= 5 %) birds)))

(defn check-odds [birds]
  (every? #(== 0 %) (keep-indexed #(if (odd? %1) %2) birds)))

(defn check-even [birds]
  (every? #(== 1 %) (keep-indexed #(if (even? %1) %2) birds)))

(defn odd-week? [birds]
  (and (check-even birds) (check-odds birds)))
