mkdir sem1
mkdir sem2

mv 3d.pdf atps*.pdf growth.pdf mid1.pdf mid2.pdf polar.pdf prob*.pdf vect*.pdf sem1/
mv gatm*.pdf limits*.pdf matrices1.pdf mid1_.pdf mid2_.pdf sem2/

# rename matrices1 to matrices, since for some reason it's considered 1 out of 1
mv sem2/matrices1.pdf sem2/matrices.pdf

# rename mid1_, mid2_ to mid1, mid2
mv sem2/mid1_.pdf sem2/mid1.pdf
mv sem2/mid2_.pdf sem2/mid2.pdf
