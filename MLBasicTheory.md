# Machine Learning Basic Theory Notes
 

Machine Learning is a subfield in computer science dedicated to build systems that can "*learn*" by analising data without being explicity programmed and it gets better by evaluating itslef with a performance measure.

## Classification of Machine Learning Systems

### Classified by: Wheter it was Supervised by a human or not

#### Supervised Learning

Supervised learning means that it's completeley controlled by a human what data is feed to the algorithm, meaning that a human indicates a what results are expected with the data feed. "*Data is labeled by a human*".

Examples:

- Decision Trees
- Random Forests
- k-Nearest Neighbors
- Linear Regression
- Logistic Regression
- Support Vector Machines

#### Unsupervised Learning 

Unsupervised learning means that the data feed to the algorithm doesn't know what results we expect to get with that data. "*Unlabeled Data*".

Examples:

- K-means
- Gaussian Mixture Models
- Mean Shift

#### Semisupervised Learning

Semisupervised learning means that some of the data comes with it's expected results but some as well comes without them. This is achieved by combining supervised and unsupervised algorithms. "*The data is not entirely labeled*"

#### Reinforcement Learning 

Reinforcement Learning means that the learning system(*agent*) can detect the "*environment*" and make desicions to increase the "*rewards*" and decrease the "*penalties*", these desicions are called "*policy*". "*The system can choose actions and either gets rewarded or penalized by those actions, then it tries to repeat actions that get rewarded and avoid the ones that penalizes it*".

- Q-Learning algorithm
- [Check OpenAI Gym][1]


### Classified by: wheter it can keep learning or not

#### Batch Learning / Offline Learning

Batch learning  means that the system must be trained using all the available data in one go, it's also called Offline learning because the training is usually done when the system is not in "*production*" (is not active for the final users). Once it finishes it's training it will only apply what it learned in the training phase and will not learn while it's being used.

**Disadvantages:** if the data is large and varies greatly in short periods of time it'll become impossible to mantain due to high resource consumption on training(*time and/or computional power*).

#### Online Learning
Online learning means that the system is trained incrementally by feeding it data sequentially. The learning is done in "*steps*" that are fast and cheap in resources so the system can keep learning about new data as soon it becomes available to it.

Online learning algorithms can be used to perform "*out-of-core learning*", which basically means that the data is so large it wouldn't fit in a single machine(RAM) if it were to load it completely.

**Disadvantages:** The learning rate is very important to tune, since it'll determine wheter the system will priorize old data or the newest data.





[1]: https://gym.openai.com/
