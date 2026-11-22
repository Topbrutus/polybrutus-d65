#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
c=json.loads((R/'results/certificate_d65.json').read_text('utf8'))
m=json.loads((R/'publication/zenodo_metadata_blueprint.json').read_text('utf8'))
assert c['status']=='PASS' and c['dimension']==m['scientific_dimension']==65
assert c['vertices']==m['norm_one_vertices']==70
assert c['pairs']==m['exact_labelled_squared_pairs']==2415
assert c['affine_rank']==c['centered_gram_rank']==65
assert c['eigenvalue_35_multiplicity']==m['model_eigenvalue_35_multiplicity']==59
assert c['eigenvalue_69_over_2_multiplicity']==m['model_eigenvalue_69_over_2_multiplicity']==4
assert c['parent_tag_commit']=='acc49976f17add61804888d15f3e1898e549ce60'
assert c['parent_doi']==m['scientific_parent_doi']=='10.5281/zenodo.24432481'
assert m['related_identifiers']==[{'identifier':'10.5281/zenodo.24432481','relation':'isDerivedFrom','resource_type':'publication-preprint','scheme':'doi'}]
assert len(m['keywords'])==9
assert 'affine Euclidean dimension sixty-five' in m['keywords']
assert 'fifty-ninefold ideal eigenvalue' in m['keywords']
assert len(m['references'])==2
assert '10.5281/zenodo.24432481' in m['references'][0]
assert '10.5281/zenodo.24407952' in m['references'][1]
assert not set(m['keywords']).intersection({'affine Euclidean dimension sixty-four','fifty-eightfold ideal eigenvalue','affine Euclidean dimension sixty-six','sixtyfold ideal eigenvalue'})
note=(R/'publication/POLYBRUTUS_65D_NOTE.md').read_text('utf8')
assert all(x in note for x in ('## References','10.5281/zenodo.24432481','10.5281/zenodo.24407952'))
print('D65_CURRENT_9_KEYWORDS_STRUCTURED_DIRECT_D64_PARENT_AND_SEPARATE_D64_D7_REFERENCES_PASS')
