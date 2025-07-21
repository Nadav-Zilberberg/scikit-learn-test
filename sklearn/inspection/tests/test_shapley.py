import pytest
from sklearn.inspection import ShapleyValueExplainer
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification


def test_shapley_value_explainer_basic():
    X, y = make_classification(n_samples=100, n_features=10, random_state=42)
    clf = RandomForestClassifier(random_state=42).fit(X, y)

    explainer = ShapleyValueExplainer(estimator=clf)
    explainer.fit(X)

    with pytest.raises(NotImplementedError, match="Shapley value computation not yet implemented."):
        explainer.transform(X[:5])

