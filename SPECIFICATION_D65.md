# Polybrutus D65 — exact 70-point labelled Euclidean squared-distance metric

**Exclusive direct parent scientific source:** Topbrutus/polybrutus-d64@v0.1.0, actual peeled scientific Git commit \`acc49976f17add61804888d15f3e1898e549ce60\`, DOI 10.5281/zenodo.24432481, original full source ZIP SHA256 \`c43fdc3487fd226eb63d790f3bd4e7e26afb84b58d8b8947b0ad2a265c2dce71\`, original D64 certificate SHA256 \`ad281b486054b8e756a3d30d8b5a4b0ce313f07310b6cc94940f1dc841100207\`.

## Conservative perpendicular norm-one extension

Embed all 69 predecessor norm-one vectors p_i as q_i=(p_i,0). Append one perpendicular unit vector q_70. Every one of C(69,2)=2346 old labelled squared distances remains unchanged; all 69 new squared distances equal 2R². Total C(70,2)=2415 labelled unordered pairs.

Construct a rational Gram G as orthogonal sum of seven original canonical norm-one points (Gram rank 3), a separate centered five-point regular unit simplex (rank 4) with mutual inner products -1/4, and **58** independent mutually orthogonal norm-one axes (rank 58). Hence G=XXᵀ is PSD, unit diagonal, exact rank **3+4+58=65**. Set D_ii=0 and D_ij=2-2G_ij. With H=I-11ᵀ/70, B=-(HDH)/2=HGH is PSD of rank **65**. An inherited canonical antipodal point pair implies the origin lies in the affine hull. Minimum affine Euclidean dimension of this particular metric is therefore 65 (66 coordinate storage).

At R=1, \`k=4d²/R²\` exact histogram: 4:6, 7:2, 8:2384, 9:3, 10:10, 12:6, 13:2, 16:2; total 2415. Exact sum of squared pair distances R=1: **19367/4**.

## Independently stipulated ideal weighted graph

Freely choose scalar unit masses, weighted complete edges w_ij=1/d_ij². New point connects to all 69 old points with weight 1/2. The chosen ideal Laplacian is L65=[[L64+I69/2,-1_69/2],[-1_69ᵀ/2,69/2]]. Its characteristic recurrence is chi70(z)=z(z-35)chi69(z-1/2)/(z-1/2).
Using the inherited seven-point factor f6(z)=chiP7(z)/z:
chi70(z)=z(z-35)^59(z-69/2)^4*f6(z-63/2).
Exact rational nullities yield Laplacian eigenvalue **35 multiplicity 59**, and **69/2 multiplicity 4**. These values are dimensionless model eigenmodes, not physical frequencies.

**Bibliography:** immediate D64 DOI 10.5281/zenodo.24432481; historical D7 DOI 10.5281/zenodo.24407952.
