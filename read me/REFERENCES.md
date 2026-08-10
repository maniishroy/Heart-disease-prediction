# HeartCheck DL - References & Resources

## 📚 Complete Reference Links Used in Project Development

---

## 1. Dataset Sources

### Primary Dataset
**Kaggle Heart Failure Prediction Dataset**
- **Link**: https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction
- **Author**: fedesoriano
- **Description**: Combines 5 heart disease datasets (918 observations, 11 features + 1 target)
- **License**: CC0: Public Domain
- **Usage**: Primary training data for heart disease prediction model

### Original Data Sources (Combined in Kaggle Dataset)
1. **Cleveland Heart Disease Database**
   - **Link**: https://archive.ics.uci.edu/ml/datasets/heart+disease
   - **Source**: UCI Machine Learning Repository
   - **Institution**: Cleveland Clinic Foundation

2. **Hungarian Institute of Cardiology, Budapest**
   - **Link**: https://archive.ics.uci.edu/ml/datasets/heart+disease
   - **Contributor**: Andras Janosi, M.D.

3. **University Hospital, Zurich, Switzerland**
   - **Link**: https://archive.ics.uci.edu/ml/datasets/heart+disease
   - **Contributor**: William Steinbrunn, M.D.

4. **University Hospital, Basel, Switzerland**
   - **Link**: https://archive.ics.uci.edu/ml/datasets/heart+disease
   - **Contributor**: Matthias Pfisterer, M.D.

5. **V.A. Medical Center, Long Beach, CA**
   - **Link**: https://archive.ics.uci.edu/ml/datasets/heart+disease
   - **Contributor**: Robert Detrano, M.D., Ph.D.

---

## 2. Machine Learning Frameworks & Libraries

### Deep Learning
**TensorFlow & Keras**
- **Official Website**: https://www.tensorflow.org/
- **Documentation**: https://www.tensorflow.org/api_docs
- **GitHub**: https://github.com/tensorflow/tensorflow
- **Tutorial Used**: https://www.tensorflow.org/tutorials/keras/classification
- **Version**: 2.15.0
- **Purpose**: Neural network implementation (MLP architecture)

**PyTorch (Alternative Option)**
- **Official Website**: https://pytorch.org/
- **Documentation**: https://pytorch.org/docs/stable/index.html
- **GitHub**: https://github.com/pytorch/pytorch
- **Tutorial**: https://pytorch.org/tutorials/beginner/basics/intro.html
- **Purpose**: Alternative deep learning framework

### Machine Learning Libraries
**Scikit-learn**
- **Official Website**: https://scikit-learn.org/
- **Documentation**: https://scikit-learn.org/stable/documentation.html
- **GitHub**: https://github.com/scikit-learn/scikit-learn
- **User Guide**: https://scikit-learn.org/stable/user_guide.html
- **Version**: 1.3.0+
- **Purpose**: Data preprocessing, encoding, scaling, metrics

**Key Modules Used**:
- Preprocessing: https://scikit-learn.org/stable/modules/preprocessing.html
- Model Selection: https://scikit-learn.org/stable/modules/cross_validation.html
- Metrics: https://scikit-learn.org/stable/modules/model_evaluation.html

---

## 3. Web Framework

### Flask
**Flask Web Framework**
- **Official Website**: https://flask.palletsprojects.com/
- **Documentation**: https://flask.palletsprojects.com/en/3.0.x/
- **GitHub**: https://github.com/pallets/flask
- **Quickstart Guide**: https://flask.palletsprojects.com/en/3.0.x/quickstart/
- **Version**: 3.0.0+
- **Purpose**: Backend web application, API endpoints

**Flask Extensions Used**:
- Flask-CORS: https://flask-cors.readthedocs.io/
- Werkzeug Security: https://werkzeug.palletsprojects.com/en/3.0.x/utils/#module-werkzeug.security

---

## 4. Data Processing Libraries

### Pandas
- **Official Website**: https://pandas.pydata.org/
- **Documentation**: https://pandas.pydata.org/docs/
- **GitHub**: https://github.com/pandas-dev/pandas
- **User Guide**: https://pandas.pydata.org/docs/user_guide/index.html
- **Version**: 2.0.0+
- **Purpose**: Data manipulation, CSV loading, DataFrame operations

### NumPy
- **Official Website**: https://numpy.org/
- **Documentation**: https://numpy.org/doc/stable/
- **GitHub**: https://github.com/numpy/numpy
- **User Guide**: https://numpy.org/doc/stable/user/index.html
- **Version**: 1.24.0+
- **Purpose**: Numerical computations, array operations

---

## 5. Academic Papers & Research

### Neural Networks & Deep Learning

**1. Backpropagation Algorithm**
- **Title**: "Learning representations by back-propagating errors"
- **Authors**: Rumelhart, D. E., Hinton, G. E., & Williams, R. J.
- **Year**: 1986
- **Journal**: Nature, 323(6088), 533-536
- **DOI**: https://doi.org/10.1038/323533a0
- **Link**: https://www.nature.com/articles/323533a0

**2. Adam Optimizer**
- **Title**: "Adam: A Method for Stochastic Optimization"
- **Authors**: Kingma, D. P., & Ba, J.
- **Year**: 2014
- **Conference**: ICLR 2015
- **arXiv**: https://arxiv.org/abs/1412.6980
- **PDF**: https://arxiv.org/pdf/1412.6980.pdf

**3. Batch Normalization**
- **Title**: "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift"
- **Authors**: Ioffe, S., & Szegedy, C.
- **Year**: 2015
- **Conference**: ICML 2015
- **arXiv**: https://arxiv.org/abs/1502.03167
- **PDF**: https://arxiv.org/pdf/1502.03167.pdf

**4. Dropout Regularization**
- **Title**: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"
- **Authors**: Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I., & Salakhutdinov, R.
- **Year**: 2014
- **Journal**: Journal of Machine Learning Research, 15(1), 1929-1958
- **Link**: https://jmlr.org/papers/v15/srivastava14a.html
- **PDF**: https://jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf

**5. ReLU Activation Function**
- **Title**: "Rectified Linear Units Improve Restricted Boltzmann Machines"
- **Authors**: Nair, V., & Hinton, G. E.
- **Year**: 2010
- **Conference**: ICML 2010
- **Link**: https://icml.cc/Conferences/2010/papers/432.pdf

### Medical AI & Healthcare Applications

**6. Heart Disease Prediction Using Machine Learning**
- **Title**: "Heart Disease Prediction Using Machine Learning Algorithms"
- **Authors**: Mohan, S., Thirumalai, C., & Srivastava, G.
- **Year**: 2019
- **Journal**: Procedia Computer Science, 165, 764-773
- **DOI**: https://doi.org/10.1016/j.procs.2020.01.032
- **Link**: https://www.sciencedirect.com/science/article/pii/S1877050920300557

**7. Deep Learning in Healthcare**
- **Title**: "A guide to deep learning in healthcare"
- **Authors**: Esteva, A., Robicquet, A., Ramsundar, B., et al.
- **Year**: 2019
- **Journal**: Nature Medicine, 25(1), 24-29
- **DOI**: https://doi.org/10.1038/s41591-018-0316-z
- **Link**: https://www.nature.com/articles/s41591-018-0316-z

**8. Clinical AI Ethics**
- **Title**: "The ethics of artificial intelligence in health care"
- **Authors**: Char, D. S., Shah, N. H., & Magnus, D.
- **Year**: 2018
- **Journal**: Journal of the American Medical Informatics Association, 25(11), 1404-1406
- **DOI**: https://doi.org/10.1093/jamia/ocy068
- **Link**: https://academic.oup.com/jamia/article/25/11/1404/5074292

---

## 6. Technology Stack Documentation

### Python
- **Official Website**: https://www.python.org/
- **Documentation**: https://docs.python.org/3/
- **Version**: 3.11+
- **Tutorial**: https://docs.python.org/3/tutorial/

### HTML5 & CSS3
- **MDN Web Docs**: https://developer.mozilla.org/en-US/docs/Web
- **HTML Reference**: https://developer.mozilla.org/en-US/docs/Web/HTML
- **CSS Reference**: https://developer.mozilla.org/en-US/docs/Web/CSS

### JavaScript
- **MDN JavaScript Guide**: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide
- **JavaScript Reference**: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference

### SQLite
- **Official Website**: https://www.sqlite.org/
- **Documentation**: https://www.sqlite.org/docs.html
- **Tutorial**: https://www.sqlitetutorial.net/

---

## 7. Design & UI Resources

### Fonts
**Google Fonts**
- **Poppins**: https://fonts.google.com/specimen/Poppins
- **Inter**: https://fonts.google.com/specimen/Inter
- **Font Usage Guide**: https://fonts.google.com/knowledge

### Color Theory
- **Coolors Color Palette Generator**: https://coolors.co/
- **Adobe Color Wheel**: https://color.adobe.com/create/color-wheel

### CSS Techniques
**Glassmorphism**
- **CSS Glass**: https://css.glass/
- **Tutorial**: https://hype4.academy/articles/design/glassmorphism-in-user-interfaces

**Gradient Backgrounds**
- **CSS Gradient**: https://cssgradient.io/
- **WebGradients**: https://webgradients.com/

**Animations**
- **Animate.css**: https://animate.style/
- **CSS Animation Guide**: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations

---

## 8. Development Tools & Platforms

### Version Control
**Git**
- **Official Website**: https://git-scm.com/
- **Documentation**: https://git-scm.com/doc
- **Pro Git Book**: https://git-scm.com/book/en/v2

**GitHub**
- **Official Website**: https://github.com/
- **GitHub Docs**: https://docs.github.com/

### Containerization
**Docker**
- **Official Website**: https://www.docker.com/
- **Documentation**: https://docs.docker.com/
- **Get Started Guide**: https://docs.docker.com/get-started/
- **Docker Hub**: https://hub.docker.com/

**Docker Compose**
- **Documentation**: https://docs.docker.com/compose/
- **Compose File Reference**: https://docs.docker.com/compose/compose-file/

### Package Management
**pip (Python Package Installer)**
- **Documentation**: https://pip.pypa.io/en/stable/
- **PyPI**: https://pypi.org/

**Kaggle API**
- **Documentation**: https://github.com/Kaggle/kaggle-api
- **Setup Guide**: https://www.kaggle.com/docs/api

---

## 9. Tutorials & Learning Resources

### TensorFlow/Keras Tutorials
1. **Binary Classification Tutorial**
   - https://www.tensorflow.org/tutorials/keras/classification

2. **Save and Load Models**
   - https://www.tensorflow.org/tutorials/keras/save_and_load

3. **Overfit and Underfit**
   - https://www.tensorflow.org/tutorials/keras/overfit_and_underfit

### Flask Tutorials
1. **Flask Mega-Tutorial (Miguel Grinberg)**
   - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

2. **Flask Official Tutorial**
   - https://flask.palletsprojects.com/en/3.0.x/tutorial/

3. **Flask RESTful API Design**
   - https://flask-restful.readthedocs.io/en/latest/

### Machine Learning Courses
1. **Scikit-learn Tutorials**
   - https://scikit-learn.org/stable/tutorial/index.html

2. **Google Machine Learning Crash Course**
   - https://developers.google.com/machine-learning/crash-course

3. **Fast.ai Practical Deep Learning**
   - https://course.fast.ai/

4. **Coursera: Deep Learning Specialization (Andrew Ng)**
   - https://www.coursera.org/specializations/deep-learning

---

## 10. Medical & Healthcare Standards

### Clinical Data Standards
**HL7 FHIR (Fast Healthcare Interoperability Resources)**
- **Official Website**: https://www.hl7.org/fhir/
- **Documentation**: https://www.hl7.org/fhir/documentation.html

**HIPAA Compliance**
- **HHS Official Guide**: https://www.hhs.gov/hipaa/index.html
- **HIPAA for Developers**: https://www.hhs.gov/hipaa/for-professionals/special-topics/health-information-technology/index.html

### Medical Terminology
**MeSH (Medical Subject Headings)**
- **Official Website**: https://www.ncbi.nlm.nih.gov/mesh/
- **Browser**: https://meshb.nlm.nih.gov/

**SNOMED CT**
- **Official Website**: https://www.snomed.org/
- **Browser**: https://browser.ihtsdotools.org/

---

## 11. Performance & Optimization

### Model Optimization
**TensorFlow Model Optimization Toolkit**
- **Documentation**: https://www.tensorflow.org/model_optimization
- **Pruning Guide**: https://www.tensorflow.org/model_optimization/guide/pruning
- **Quantization Guide**: https://www.tensorflow.org/model_optimization/guide/quantization

### Web Performance
**Google PageSpeed Insights**
- **Tool**: https://pagespeed.web.dev/
- **Documentation**: https://developers.google.com/speed/docs/insights/v5/about

**WebPageTest**
- **Tool**: https://www.webpagetest.org/
- **Documentation**: https://docs.webpagetest.org/

---

## 12. Security Resources

### Web Security
**OWASP (Open Web Application Security Project)**
- **Official Website**: https://owasp.org/
- **Top 10 Web Application Security Risks**: https://owasp.org/www-project-top-ten/
- **OWASP Cheat Sheet Series**: https://cheatsheetseries.owasp.org/

### Flask Security
**Flask Security Best Practices**
- **Official Guide**: https://flask.palletsprojects.com/en/3.0.x/security/
- **Flask-Security Documentation**: https://flask-security-too.readthedocs.io/

### GDPR Compliance
**GDPR Official Text**
- **Link**: https://gdpr-info.eu/
- **EU Official Site**: https://ec.europa.eu/info/law/law-topic/data-protection_en

---

## 13. API & Web Standards

### REST API Design
**RESTful API Design Guide**
- **Microsoft API Guidelines**: https://github.com/microsoft/api-guidelines
- **Google API Design Guide**: https://cloud.google.com/apis/design

### HTTP Status Codes
**MDN HTTP Status Codes**
- **Reference**: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

### JSON
**JSON.org**
- **Official Website**: https://www.json.org/json-en.html
- **RFC 8259**: https://datatracker.ietf.org/doc/html/rfc8259

---

## 14. Visualization & Charts

### Chart.js
- **Official Website**: https://www.chartjs.org/
- **Documentation**: https://www.chartjs.org/docs/latest/
- **GitHub**: https://github.com/chartjs/Chart.js
- **Samples**: https://www.chartjs.org/docs/latest/samples/

### Matplotlib (Python)
- **Official Website**: https://matplotlib.org/
- **Documentation**: https://matplotlib.org/stable/contents.html
- **Tutorials**: https://matplotlib.org/stable/tutorials/index.html

---

## 15. Testing & Validation

### Python Testing
**Pytest**
- **Official Website**: https://pytest.org/
- **Documentation**: https://docs.pytest.org/en/stable/

**Unittest**
- **Python Documentation**: https://docs.python.org/3/library/unittest.html

### Web Testing
**Selenium**
- **Official Website**: https://www.selenium.dev/
- **Python Bindings**: https://selenium-python.readthedocs.io/

---

## 16. Community & Forums

### Stack Overflow
- **Website**: https://stackoverflow.com/
- **TensorFlow Tag**: https://stackoverflow.com/questions/tagged/tensorflow
- **Flask Tag**: https://stackoverflow.com/questions/tagged/flask
- **Machine Learning Tag**: https://stackoverflow.com/questions/tagged/machine-learning

### Reddit Communities
- **r/MachineLearning**: https://www.reddit.com/r/MachineLearning/
- **r/learnmachinelearning**: https://www.reddit.com/r/learnmachinelearning/
- **r/flask**: https://www.reddit.com/r/flask/
- **r/Python**: https://www.reddit.com/r/Python/

### GitHub Discussions
- **TensorFlow**: https://github.com/tensorflow/tensorflow/discussions
- **Flask**: https://github.com/pallets/flask/discussions

---

## 17. Books & Publications

### Deep Learning
1. **"Deep Learning" by Ian Goodfellow, Yoshua Bengio, and Aaron Courville**
   - **Link**: https://www.deeplearningbook.org/
   - **Free Online**: https://www.deeplearningbook.org/

2. **"Neural Networks and Deep Learning" by Michael Nielsen**
   - **Link**: http://neuralnetworksanddeeplearning.com/
   - **Free Online**: http://neuralnetworksanddeeplearning.com/

### Machine Learning
3. **"Hands-On Machine Learning" by Aurélien Géron**
   - **GitHub**: https://github.com/ageron/handson-ml3
   - **Publisher**: O'Reilly Media

4. **"Pattern Recognition and Machine Learning" by Christopher Bishop**
   - **Publisher**: Springer
   - **Website**: https://www.microsoft.com/en-us/research/people/cmbishop/

### Flask & Web Development
5. **"Flask Web Development" by Miguel Grinberg**
   - **Publisher**: O'Reilly Media
   - **Author's Blog**: https://blog.miguelgrinberg.com/

---

## 18. Model Evaluation Tools

### Scikit-learn Metrics
- **Classification Report**: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html
- **Confusion Matrix**: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
- **ROC AUC Score**: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html
- **Precision, Recall, F1**: https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics

### TensorFlow Metrics
- **Keras Metrics**: https://www.tensorflow.org/api_docs/python/tf/keras/metrics
- **Model Evaluation**: https://www.tensorflow.org/guide/keras/train_and_evaluate

---

## 19. Data Visualization for Presentations

### Matplotlib/Seaborn
- **Seaborn**: https://seaborn.pydata.org/
- **Gallery**: https://seaborn.pydata.org/examples/index.html

### Plotly
- **Official Website**: https://plotly.com/python/
- **Documentation**: https://plotly.com/python/getting-started/

---

## 20. Deployment & Hosting

### Cloud Platforms
**Heroku**
- **Official Website**: https://www.heroku.com/
- **Python Deployment**: https://devcenter.heroku.com/articles/getting-started-with-python

**AWS (Amazon Web Services)**
- **Official Website**: https://aws.amazon.com/
- **EC2 Documentation**: https://docs.aws.amazon.com/ec2/
- **Elastic Beanstalk**: https://docs.aws.amazon.com/elasticbeanstalk/

**Google Cloud Platform**
- **Official Website**: https://cloud.google.com/
- **App Engine**: https://cloud.google.com/appengine/docs

**Azure**
- **Official Website**: https://azure.microsoft.com/
- **Web Apps**: https://azure.microsoft.com/en-us/services/app-service/web/

### Production Servers
**Gunicorn**
- **Official Website**: https://gunicorn.org/
- **Documentation**: https://docs.gunicorn.org/en/stable/

**Nginx**
- **Official Website**: https://nginx.org/
- **Documentation**: https://nginx.org/en/docs/

---

## 21. Accessibility Standards

### WCAG (Web Content Accessibility Guidelines)
- **Official Website**: https://www.w3.org/WAI/standards-guidelines/wcag/
- **Quick Reference**: https://www.w3.org/WAI/WCAG21/quickref/

### ARIA (Accessible Rich Internet Applications)
- **MDN ARIA Guide**: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA
- **W3C Specification**: https://www.w3.org/TR/wai-aria/

---

## 22. Additional Resources

### Kaggle Learn
- **Python**: https://www.kaggle.com/learn/python
- **Intro to Machine Learning**: https://www.kaggle.com/learn/intro-to-machine-learning
- **Intermediate Machine Learning**: https://www.kaggle.com/learn/intermediate-machine-learning
- **Deep Learning**: https://www.kaggle.com/learn/intro-to-deep-learning

### arXiv (Research Papers)
- **Official Website**: https://arxiv.org/
- **Machine Learning Papers**: https://arxiv.org/list/cs.LG/recent
- **Computer Vision**: https://arxiv.org/list/cs.CV/recent

### Papers with Code
- **Official Website**: https://paperswithcode.com/
- **Heart Disease Datasets**: https://paperswithcode.com/datasets?q=heart+disease
- **Medical AI**: https://paperswithcode.com/area/medical

---

## 23. Inspiration & Similar Projects

### GitHub Repositories
1. **Heart Disease Prediction Projects**: https://github.com/topics/heart-disease-prediction
2. **Medical AI Projects**: https://github.com/topics/medical-ai
3. **Flask ML Projects**: https://github.com/topics/flask-machine-learning

### Kaggle Notebooks
- **Heart Disease Prediction Notebooks**: https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction/code

---

## Citation Format

### For Academic Use

**APA Format**:
```
HeartCheck DL Development Team. (2025). HeartCheck DL: Full-Stack Deep Learning 
Heart Disease Detector. Retrieved from https://github.com/yourusername/HeartCheckDL
```

**IEEE Format**:
```
[1] HeartCheck DL Development Team, "HeartCheck DL: Full-Stack Deep Learning 
Heart Disease Detector," GitHub repository, 2025. [Online]. 
Available: https://github.com/yourusername/HeartCheckDL
```

**MLA Format**:
```
HeartCheck DL Development Team. "HeartCheck DL: Full-Stack Deep Learning 
Heart Disease Detector." GitHub, 2025, https://github.com/yourusername/HeartCheckDL
```

---

## License Information

### Dataset License
- **Kaggle Dataset**: CC0: Public Domain
- **Link**: https://creativecommons.org/publicdomain/zero/1.0/

### Project License
- **MIT License**: https://opensource.org/licenses/MIT
- **Full Text**: See LICENSE file in repository

---

## Acknowledgments

Special thanks to:
- TensorFlow and Keras development teams
- Scikit-learn contributors
- Flask and Pallets Projects
- Kaggle community and dataset providers
- UCI Machine Learning Repository
- Open source community

---

**Document Version**: 1.0  
**Last Updated**: November 26, 2025  
**Maintained By**: HeartCheck DL Development Team

---

## Quick Reference Summary

| Category | Primary Resources |
|----------|------------------|
| **Dataset** | Kaggle Heart Failure Prediction Dataset |
| **Deep Learning** | TensorFlow 2.15, Keras API |
| **ML Library** | Scikit-learn 1.3+ |
| **Web Framework** | Flask 3.0 |
| **Data Processing** | Pandas, NumPy |
| **Database** | SQLite |
| **Containerization** | Docker, Docker Compose |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Fonts** | Google Fonts (Poppins, Inter) |
| **Visualization** | Chart.js, Matplotlib |

---

**For more information, refer to the individual documentation of each tool/library.**

**End of References Document**
