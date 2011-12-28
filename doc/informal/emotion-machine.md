#[Emotion machine](http://en.wikipedia.org/wiki/Emotion_machine)
Solution is based on Marvin Minsky [Emotion machine/7. Thinking chapter.](http://web.media.mit.edu/~minsky/E7/eb7.html)

![Critics with Selectors](http://web.media.mit.edu/~minsky/E7/eb7_files/image003.png)

Mainly the Thinking is split on two sections Critics and Selectors(Way to Think):

Critics are applied sequentially and indicates proper Way to Think.

### Design scratch

### Use cases

#### Training

![Train](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/UseCaseTrain.png)

Train mainly is supervised automatic with the Request and Solution pairs provided by TSS. After some essential learning
TSS monitors the Solution-s of the system.

#### Production
![Production](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/UseCaseProduction.png)

_Simplest way is the direct instruction processing._
The Learned Reactive Critics is activated and retrieve the Knowing How way of thinking.


#### Component diagram

![Component](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/Component.png)

