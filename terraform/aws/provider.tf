# Here you can define terraform provider and provider-specific values

# If you want to change "aws" provider to some other be sure to change
# provider-versions.tf in order to make everything transparent
provider "aws" {
  profile = "default"
  region  = "us-east-1"
}
