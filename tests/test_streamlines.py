import pandas as pd
import pytest

from brainrender import Scene
from brainrender.actors.streamlines import (
    Streamlines,
    make_streamlines,
)
from brainrender.atlas_specific import get_streamlines_for_region


@pytest.mark.xfail(reason="Likely due to fail due to neuromorpho")
def test_download():
    streams = get_streamlines_for_region("TH", force_download=False)
    assert len(streams) == 54
    assert isinstance(streams[0], pd.DataFrame)


@pytest.mark.xfail(reason="Likely due to fail due to neuromorpho")
def test_download_slow():
    streams = get_streamlines_for_region("TH", force_download=True)
    assert len(streams) == 54
    assert isinstance(streams[0], pd.DataFrame)


@pytest.mark.xfail(reason="Likely due to fail due to neuromorpho")
def test_streamlines():
    s = Scene(title="BR")
    streams = get_streamlines_for_region("TH", force_download=False)
    s.add(Streamlines(streams[0]))
    s.add(*make_streamlines(*streams[1:3]))

    with pytest.raises(TypeError):
        Streamlines([1, 2, 3])

    del s
