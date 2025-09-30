ECHO Build docker image
call docker build --platform linux/arm64 --provenance false -t qpcr_ge_analysis_image:latest .
call docker tag qpcr_ge_analysis_image:latest 160885287007.dkr.ecr.us-east-2.amazonaws.com/qpcr_ge_analysis_repo:latest

ECHO Authenticate docker to ECR
call aws ecr get-login-password --region us-east-2 --profile takara-instrument-admin | docker login ^
  --username AWS --password-stdin 160885287007.dkr.ecr.us-east-2.amazonaws.com

ECHO Create ECR repo
call aws ecr create-repository --repository-name qpcr_ge_analysis_repo --region us-east-2 ^
  --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE --profile takara-instrument-admin

ECHO Push docker image to ECR
call docker push 160885287007.dkr.ecr.us-east-2.amazonaws.com/qpcr_ge_analysis_repo:latest

ECHO Create Lambda function
call aws lambda create-function --function-name qpcr_ge_analysis_lambda --package-type Image ^
  --code ImageUri=160885287007.dkr.ecr.us-east-2.amazonaws.com/qpcr_ge_analysis_repo:latest ^
  --role arn:aws:iam::160885287007:role/takara_instrument_lambda_role ^
  --profile takara-instrument-admin ^
  --architectures arm64 ^
  --memory-size 4096 ^
  --timeout 60
