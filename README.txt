

# create HOTregions.ce10.bed
./regionsToBed.py
# liftOver to ce11
liftOver HOTregions.ce10.bed ~/local/support_data/ce10/ce10ToCe11.over.chain.gz HOTregions.ce11.bed HOTregions.ce10.unmapped



