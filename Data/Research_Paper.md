# How the US Presidential Elections and the Capitol Attack Shaped the

# Online Hate Landscape

## AKSHAY VERMA,George Washington University,

## PLACE HOLDER,Place holder, Place holder

```
ABSTRACT: In the digital age, online hate networks thrive as platforms for
spreading extremist ideologies and hate speech, posing a significant threat to
societal cohesion. This study examines the impact of key real-world events,
notably the 2020 U.S. presidential election and the January 6 Capitol attack,
on the evolution of online hate networks.
Using data collected from hate communities between November 1, 2020,
and January 10, 2021, this research analyzes shifts in hate speech themes and
network topology. Following the presidential election, an increase in hate
speech targeting immigration, ethnicity, and antisemitism was observed.
The January 6 Capitol attack further intensified these trends.
Central to this investigation is the examination of two key aspects of
online hate networks: the content they disseminate and the underlying
structure of their connections. By studying shifts in hate themes and network
topology, including changes in centrality and community structure, this
study seeks to uncover the mechanisms driving the evolution of online
hate networks.The analysis reveals significant changes in network cohesion
post-attack, characterized by increased clustering and assortativity.
This research sheds light on the role of online platforms in radicalization
and mobilization efforts, emphasizing the need for proactive measures to
combat hate speech online. Despite its niche presence, Telegram has become
a key hub for propagating extremist ideologies and coordinating malicious
activities.
```
## 1 INTRODUCTION

```
In the digital age, the internet has become a breeding ground for
the dissemination of hate speech and extremist ideologies, fostering
the formation of online hate networks [ 1 ]. These networks, charac-
terized by their interconnected web of individuals sharing common
ideologies rooted in hatred and discrimination, pose a significant
threat to societal harmony and individual safety. Understanding the
dynamics of these networks is paramount in combating the prolif-
eration of hate speech and mitigating its harmful consequences.
This research looks into the intricate relationship between polar-
izing real-world events and the evolution of online hate networks.
By analysing the activities of hate communities online, this study
aims to show how these networks undergo a transformation in the
aftermath of pivotal events, specifically this research looks at the
2020 presidential election and the January 6 Capitol attack in the
United States.
The highly contentious 2020 US presidential election, exacerbated
by the proliferation of misinformation and divisive rhetoric, served
as a catalyst for amplifying existing tensions within online commu-
nities [ 2 ]. Subsequently, the violent insurrection at the Capitol on
January 6, 2021, further underscored the potency of online platforms
as breeding grounds for radicalization and mobilization.
Central to this investigation is the analysis of two key facets
of online hate networks: the content disseminated within these
networks and the underlying topology of the network. By examining
Authors’ addresses: Akshay Verma, averma29@gwu.edu, George Washington Uni-
versity, , , , , ; Place holder, Place holder, Place holder, Place holder, Place holder,
Placeholder.
```
```
shifts in hate themes within hate communities, we aim to discern
patterns of adaptation in response to external triggers. Furthermore,
by examining alterations in network topology, including changes
in centrality, community structure, and clustering, we seek to work
out the structural dynamics driving the evolution of online hate
networks.
```
## 2 DATA

```
The data for this study was collected by the Dynamic Online Net-
work Lab at George Washington University (GWU). Data collection
commenced with the identification of online hate communities, fol-
lowed by continuous monitoring for cross-posts. For instance, if a
user in a hate community posted a link to another community, a
directed edge was established from the hate community towards
the linked community.
```
```
Fig. 1. Representation of how links are assigned in the network
```
```
While all the source nodes belong to identified hate communi-
ties, the target nodes may or may not belong to identified hate
communities.
This study focuses on the period surrounding the 2020 U.S. presi-
dential election and the events of January 6, 2021. Specifically, data
was analyzed from November 1, 2020, to January 10, 2021.
In addition to monitoring cross-posting activities within these
hate communities, the posts were also classified to identify various
types of hate speech prevalent within the posts. Seven types of
hate speech were classified, targeting race, gender, religion, anti-
semitism, gender identity/sexual orientation (GISO), immigration,
and ethnicity/identitarian/nationalism (EIN).
```
## 3 RESULTS

```
The analysis of the hate network following the 2020 presidential
election on Nov 3, 2020, and the United States Capitol attack on Jan
6, 2021, sheds light on the complex interplay of online dynamics and
real world events. Through an examination of network cohesion
and the change in hate content, we discover compelling insights into
the transformative forces at play within this digital hate ecosystem.
This section looks into the changes observed within the network.
```

2 • Akshay Verma and Place holder

Fig. 2. An example of cross-post of a YouTube video in a telegram channel
identified as a hate community

```
Fig. 3. Percentage increase in number of links relative to Nov 1, 2020
```
The initial observation that stood out was the substantial increase
in the number of links within the network during both time intervals.
On November 3, the day of the presidential elections, there was a
notable surge in hate links, showing a 41.6% increase compared to
November 1. Subsequently, on November 7, when Joe Biden was
declared president-elect, the number of links spiked even further,
rising by 68% compared to November 1.

```
Fig. 4. Percentage increase in number of links relative to Jan 1, 2021
```
We observed a similar spike in our network surrounding the
events of the January 6th Capitol attacks. On January 6, there was a
significant increase in the number of links, rising by 67.59% com-
pared to January 1

## 3.1 Network Cohesion

Our analysis of the network following the 2021 Jan 6 Capitol attacks
reveals a significant increase in network cohesion. This tighten-
ing of connections is evident through three key network metrics:
clustering coefficient, assortativity, and community dynamics.
The clustering coefficient, which measures the tendency of nodes
(online communities) to form triangles (connected groups of three),

```
Table 1. Comparison of Network Metrics post Jan 6 2021 Capitol Attack
```
```
Property (Jan 1 to 5, 2021)Pre Jan 6 (Jan 6 to 10, 2021)Post Jan 6 % Change
```
```
Number of
Communities^11586 -25.2%
Size of the
Largest Community^56327068 25.5%
Clustering
Coefficient 0.011 0.028 159.2%
Assortativity -0.49 -0.35 25.1%
```
```
jumped by a substantial 159% after the Jan 6 capitol attack. This
dramatic rise suggests a significant shift in the network structure.
Nodes previously on the periphery formed connections with their
neighbors, leading to a denser network with well-defined clusters.
This implies that individual nodes within the hate network became
more interconnected and entrenched within their specific groups
[3].
Furthermore, assortativity, which reflects the tendency of nodes
to connect with similar nodes, also increased by 25.1%. This rise
in assortativity strengthens the notion of increased cohesion and
homophily; Individuals within the network preferentially connected
with others who shared characteristics. This potentially indicates
a strengthening of existing ideologies within the network, foster-
ing a more homogenous and an environment resilient to outside
intervention [4] [5].
```
```
Fig. 5. Size of the largest connected component on each day during Jan 1 -
10, 2021
```
```
Finally, the observed changes in the number of communities and
the size of the largest community paint a convincing picture of
network consolidation. The number of communities decreased by a
significant 25.2%, hinting at smaller communities merging to form
larger communities. Furthermore, the size of the largest community
grew by 25.5%, suggesting a convergence of individual communities
towards a more dominant, potentially extreme, viewpoint. This
dynamic implies a less diverse network with a more unified ideology,
```

```
How the US Presidential Elections and the Capitol Attack Shaped the Online Hate Landscape • 3
```
potentially amplifying the spread of hate speech or coordinated
actions.

Fig. 6. Visualization of the pre-capitol attack network and the post-capitol
attack network

These findings on network metrics are further supported by visu-
alizations using network visualization tools like Gephi, employing
the ForceAtlas2 layout. This layout algorithm assigns forces to nodes,
attracting or repelling them based on their connections, thus shap-
ing the overall network structure. Examining these visualizations
reveals a notable shift towards a more cohesively connected network
structure.
The trends observed following the November 3, 2020 elections
exhibit a similar pattern, albeit with smaller variations compared to
those witnessed after the January 6 Capitol attack.

Table 2. Comparison of Network Metrics post the 2020 US Presidential
Election

```
Property (Nov 1 to 2, 2020)Pre Nov 3 (Nov 3 to 4, 2020)Post Nov3 % Change
```
```
Number of
Communities^7068 -2.85%
Size of the
Largest Community^43344726 9.0%
Clustering
Coefficient 0.012 0.014 12.4%
Assortativity -0.52 -0.49 5.3%
```
The relatively smaller changes observed following the 2020 elec-
tions, compared to the upheaval witnessed after the January 6 Capi-
tol attack, could potentially be attributed to the elections being a
less unexpected event, thus resulting in more moderate alterations
in the network metrics.

## 3.2 Change in Hate Content

Following the analysis of network cohesion, this subsection ex-
plores the changes in hate content within the network during the
same period (November 1, 2020 – January 10, 2021). Here, "hate
content" refers to speech targeting individuals or groups based on
characteristics like immigration status, race, or gender identity.

```
Fig. 7. Size of the largest connected component on each day during Nov 1 -
10, 2020
```
```
Fig. 8. Percentage change observed in the hate network after Nov 7, 2020.
```
```
Following the declaration of Joe Biden as president-elect on No-
vember 7, 2020, a significant uptick in hate speech targeting immigra-
tion, ethnicity, and antisemitism was detected within the network.
Particularly noteworthy were the observed increases: a 269.5% surge
in anti-immigration sentiments, a 98.7% rise in ethnically-based
hatred, and a 117.57% escalation in expressions of antisemitism be-
tween November 7 and November 11, compared to November 2 to
November 6. These trends are indicative of the immigration anx-
ieties harbored by far-right communities, which often align with
the Great Replacement conspiracy theory, attributing perceived
demographic shifts to Jewish influence [6].
Following the Capitol attack on January 6th, a comparable surge
in anti-immigration sentiments was evident, with a notable 108.69%
rise in posts containing anti-immigration messages between January
6th and January 10th, in contrast to the period of January 1st to
January 5th, 2020.
The analysis also reveals a strong correlation between the daily
link counts originating from specific social networks and the inci-
dence of hate speech detected within the network spanning from
November 1, 2020, to January 10, 2021.
```

```
4 • Akshay Verma and Place holder
```
```
Fig. 9. Percentage change observed in the hate network after Jan 6, 2021.
```
```
Fig. 10. Correlation between count of links origination from different social
networking sites and count of hate type detected in the network
```
```
Specifically, an increase in links originating from 4chan, Gab,
Twitter, and Telegram exhibits a strong correlation with instances
of hate speech targeting immigration, race, and gender and sexual
identity (GISO). While the correlation suggests a potential link be-
tween these events and the rise in hate content, further investigation
is needed to determine causality.
```
## 3.3 Role of Telegram

Following the Presidential Elections on Nov 3, Telegram emerged
as a significant player in shaping the dynamics of the hate network.
During November 4–7, there was a remarkable surge in connectivity
within the network, evidenced by a substantial 299% increase in the
number of connections involving Telegram compared to November
1–3, 2020 (from 592 to 2366). Telegram’s importance both as a tar-
get and source node within the hate network saw a considerable
rise from this volume perspective. Specifically, Telegram’s repre-
sentation as a target node increased from 18.22% to 33.47%, while

```
its presence as a source node increased from 21.73% to 37.24% of
all links present in the hate core network post-election. This rise
in Telegram’s connections highlights its growing significance as a
central platform for communication and coordination among hate
groups within the network [7].
```
```
Fig. 11. Network where Telegram is either the source or target node
```
```
One Telegram community, identified by the codename "TG__122",
warrants particular attention. "TG__122" which is now named “US
Voter Fraud & Coup-Ops Intel 2020 – 2022” was initially absent from
the network between November 1 and 3, but rapidly ascended to
become one of the most crucial and interconnected nodes within
the November 4–7 network. Moreover, "TG__122" exhibits strong
associations with two other Telegram channels, "TG__218", a right-
wing podcast, and "TG__146", a right-wing telegram channel named
"Exposing Cultural Marxism", both of which were highly active
in the network before November 3. The substantial influx of links
directed towards "TG__122" signifies its pivotal role as a central
hub for disseminating disinformation concerning the presidential
election and alleged instances of vote fraud.
Moreover, the rise of Telegram is particularly fascinating given
its relatively limited ubiquity compared to mainstream social net-
working sites in the United States. However, as reported by CNN,
Telegram has emerged as a source of concern for law enforcement
agencies due to its association with ’Q-anon’ and ’Pro-Trump Con-
spiracy theories’ [ 8 ]. Despite its niche presence, Telegram has be-
come a preferred platform for individuals seeking to propagate hate
speech and coordinate malicious activities [ 9 ]. This association fur-
ther solidifies Telegram’s significant influence on the perpetuation
of extremist ideologies and the dissemination of hate speech within
the studied network.
```
## 4 DISCUSSION

```
In conclusion, this study illuminates the changes in online hate
networks in response to significant real-world events, particularly
the 2020 U.S. presidential election and the January 6 Capitol attack.
Firstly, an increase in hate speech targeting immigration, eth-
nicity, and antisemitism following pivotal events, indicative of un-
derlying societal tensions and extremist ideologies. The observed
correlations between specific social networks and the incidence of
hate speech highlight the role of online platforms in propagating
extremist narratives. Secondly, network cohesion significantly in-
creased post-attack, evidenced by tighter clustering and homophily
within hate networks. This suggests a consolidation of extremist
```

```
How the US Presidential Elections and the Capitol Attack Shaped the Online Hate Landscape • 5
```
ideologies and a more resilient environment for hate speech dissem-
ination.
Furthermore, the rise of Telegram as a central hub within hate net-
works underscores the evolving landscape of online extremism. De-
spite its niche presence in the United States, Telegram has emerged
as a significant platform for coordinating malicious activities and
disseminating hate speech.
Overall, this research emphasizes the urgent need for proactive
measures to combat online extremism and promote digital resilience.
By understanding the mechanisms driving the evolution of online
hate networks, policymakers, researchers, and platform providers
can develop targeted interventions to mitigate the harmful conse-
quences of hate speech online and safeguard societal harmony and
individual safety.

## REFERENCES

```
[1]A. Schackmuth,Extremism, fake news and hate: effects of social media in the post-
truth era. PhD thesis, DePaul University, 2018.
```
```
[2]C. S. Lee, J. Merizalde, J. D. Colautti, J. An, and H. Kwak, “Storm the capitol: linking
offline political speech and online twitter extra-representational participation on
qanon and the january 6 insurrection,”Frontiers in Sociology, vol. 7, p. 876070, 2022.
[3] D. J. Watts,Small worlds: the dynamics of networks between order and randomness,
vol. 36. Princeton university press, 2004.
[4]P. Leifeld, “Polarization in the social sciences: Assortative mixing in social science
collaboration networks is resilient to interventions,”Physica A: Statistical Mechanics
and its Applications, vol. 507, pp. 510–523, 2018.
[5]M. Oehlers and B. Fabian, “Graph metrics for network robustness—a survey,”Math-
ematics, vol. 9, no. 8, p. 895, 2021.
[6]M. Obaidi, J. Kunst, S. Ozer, and S. Y. Kimel, “The “great replacement” conspiracy:
How the perceived ousting of whites can evoke violent extremism and islamopho-
bia,”Group Processes & Intergroup Relations, vol. 25, no. 7, pp. 1675–1695, 2022.
[7]H. Schulze, J. Hohner, S. Greipl, M. Girgnhuber, I. Desta, and D. Rieger, “Far-right
conspiracy groups on fringe platforms: A longitudinal analysis of radicalization
dynamics on telegram,”Convergence: The International Journal of Research into New
Media Technologies, vol. 28, no. 4, pp. 1103–1126, 2022.
[8]D. O. Jamie Gangel, “Talk of overturning the 2020 election on new social media
platforms used by qanon followers sparks fears of further violence,” 2021.
[9]J. Guhl and J. Davey, “A safe space to hate: White supremacist mobilisation on
telegram,”Institute for Strategic Dialogue, vol. 26, 2020.
```

