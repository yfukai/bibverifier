#!/usr/bin/env python3

import os
import click
import crossrefapi

@click.command()
@click.argument("input_file_path", type=click.File("r"))
@click.argument("output_dir", type=click.Path(resolve_path=True, file_okay=False, writable=True))
def main(
    input_file_path,
    output_dir, 
):
    if not output_dir.endswith("/"):
        output_dir += "/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(input_file_path,"r") as f:
        reference_lines = f.readlines()
    
    
    

if __name__ == "__main__":
    main()