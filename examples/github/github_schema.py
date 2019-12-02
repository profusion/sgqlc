import sgqlc.types
import sgqlc.types.datetime
import sgqlc.types.relay


github_schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
github_schema -= sgqlc.types.relay.Node
github_schema -= sgqlc.types.relay.PageInfo



########################################################################
# Scalars and Enumerations
########################################################################
class ActionExecutionCapabilitySetting(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('DISABLED', 'ALL_ACTIONS', 'LOCAL_ACTIONS_ONLY', 'NO_POLICY')


class AuditLogOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT',)


Boolean = sgqlc.types.Boolean

class CollaboratorAffiliation(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OUTSIDE', 'DIRECT', 'ALL')


class CommentAuthorAssociation(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('MEMBER', 'OWNER', 'COLLABORATOR', 'CONTRIBUTOR', 'FIRST_TIME_CONTRIBUTOR', 'FIRST_TIMER', 'NONE')


class CommentCannotUpdateReason(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ARCHIVED', 'INSUFFICIENT_ACCESS', 'LOCKED', 'LOGIN_REQUIRED', 'MAINTENANCE', 'VERIFIED_EMAIL_REQUIRED', 'DENIED')


class CommitContributionOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OCCURRED_AT', 'COMMIT_COUNT')


class ContributionOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OCCURRED_AT',)


Date = sgqlc.types.datetime.Date

DateTime = sgqlc.types.datetime.DateTime

class DefaultRepositoryPermissionField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('NONE', 'READ', 'WRITE', 'ADMIN')


class DeploymentOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT',)


class DeploymentState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ABANDONED', 'ACTIVE', 'DESTROYED', 'ERROR', 'FAILURE', 'INACTIVE', 'PENDING', 'QUEUED', 'IN_PROGRESS')


class DeploymentStatusState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('PENDING', 'SUCCESS', 'FAILURE', 'INACTIVE', 'ERROR', 'QUEUED', 'IN_PROGRESS')


class EnterpriseAdministratorInvitationOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT',)


class EnterpriseAdministratorRole(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OWNER', 'BILLING_MANAGER')


class EnterpriseDefaultRepositoryPermissionSettingValue(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('NO_POLICY', 'ADMIN', 'WRITE', 'READ', 'NONE')


class EnterpriseEnabledDisabledSettingValue(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ENABLED', 'DISABLED', 'NO_POLICY')


class EnterpriseEnabledSettingValue(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ENABLED', 'NO_POLICY')


class EnterpriseMemberOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('LOGIN', 'CREATED_AT')


class EnterpriseMembersCanCreateRepositoriesSettingValue(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('NO_POLICY', 'ALL', 'PUBLIC', 'PRIVATE', 'DISABLED')


class EnterpriseMembersCanMakePurchasesSettingValue(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ENABLED', 'DISABLED')


class EnterpriseMembershipType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ALL', 'ADMIN', 'BILLING_MANAGER', 'ORG_MEMBERSHIP')


class EnterpriseOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('NAME',)


class EnterpriseServerInstallationOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('HOST_NAME', 'CUSTOMER_NAME', 'CREATED_AT')


class EnterpriseServerUserAccountEmailOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('EMAIL',)


class EnterpriseServerUserAccountOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('LOGIN', 'REMOTE_CREATED_AT')


class EnterpriseServerUserAccountsUploadOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT',)


class EnterpriseServerUserAccountsUploadSyncState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('PENDING', 'SUCCESS', 'FAILURE')


class EnterpriseUserAccountMembershipRole(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('MEMBER', 'OWNER')


class EnterpriseUserDeployment(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CLOUD', 'SERVER')


Float = sgqlc.types.Float

class FundingPlatform(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('GITHUB', 'PATREON', 'OPEN_COLLECTIVE', 'KO_FI', 'TIDELIFT', 'COMMUNITY_BRIDGE', 'LIBERAPAY', 'ISSUEHUNT', 'OTECHIE', 'CUSTOM')


class GistOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'UPDATED_AT', 'PUSHED_AT')


class GistPrivacy(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('PUBLIC', 'SECRET', 'ALL')


class GitObjectID(sgqlc.types.Scalar):
    __schema__ = github_schema


class GitSSHRemote(sgqlc.types.Scalar):
    __schema__ = github_schema


class GitSignatureState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('VALID', 'INVALID', 'MALFORMED_SIG', 'UNKNOWN_KEY', 'BAD_EMAIL', 'UNVERIFIED_EMAIL', 'NO_USER', 'UNKNOWN_SIG_TYPE', 'UNSIGNED', 'GPGVERIFY_UNAVAILABLE', 'GPGVERIFY_ERROR', 'NOT_SIGNING_KEY', 'EXPIRED_KEY', 'OCSP_PENDING', 'OCSP_ERROR', 'BAD_CERT', 'OCSP_REVOKED')


class GitTimestamp(sgqlc.types.Scalar):
    __schema__ = github_schema


class HTML(sgqlc.types.Scalar):
    __schema__ = github_schema


ID = sgqlc.types.ID

class IdentityProviderConfigurationState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ENFORCED', 'CONFIGURED', 'UNCONFIGURED')


Int = sgqlc.types.Int

class IssueOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'UPDATED_AT', 'COMMENTS')


class IssuePubSubTopic(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('UPDATED', 'MARKASREAD', 'TIMELINE', 'STATE')


class IssueState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OPEN', 'CLOSED')


class IssueTimelineItemsItemType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ISSUE_COMMENT', 'CROSS_REFERENCED_EVENT', 'ADDED_TO_PROJECT_EVENT', 'ASSIGNED_EVENT', 'CLOSED_EVENT', 'COMMENT_DELETED_EVENT', 'CONVERTED_NOTE_TO_ISSUE_EVENT', 'DEMILESTONED_EVENT', 'LABELED_EVENT', 'LOCKED_EVENT', 'MARKED_AS_DUPLICATE_EVENT', 'MENTIONED_EVENT', 'MILESTONED_EVENT', 'MOVED_COLUMNS_IN_PROJECT_EVENT', 'PINNED_EVENT', 'REFERENCED_EVENT', 'REMOVED_FROM_PROJECT_EVENT', 'RENAMED_TITLE_EVENT', 'REOPENED_EVENT', 'SUBSCRIBED_EVENT', 'TRANSFERRED_EVENT', 'UNASSIGNED_EVENT', 'UNLABELED_EVENT', 'UNLOCKED_EVENT', 'USER_BLOCKED_EVENT', 'UNPINNED_EVENT', 'UNSUBSCRIBED_EVENT')


class LanguageOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('SIZE',)


class LockReason(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OFF_TOPIC', 'TOO_HEATED', 'RESOLVED', 'SPAM')


class MergeableState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('MERGEABLE', 'CONFLICTING', 'UNKNOWN')


class MilestoneOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('DUE_DATE', 'CREATED_AT', 'UPDATED_AT', 'NUMBER')


class MilestoneState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OPEN', 'CLOSED')


class OauthApplicationCreateAuditEntryState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ACTIVE', 'SUSPENDED', 'PENDING_DELETION')


class OauthApplicationRevokeTokensAuditEntryState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ACTIVE', 'SUSPENDED', 'PENDING_DELETION')


class OperationType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ACCESS', 'AUTHENTICATION', 'CREATE', 'MODIFY', 'REMOVE', 'RESTORE', 'TRANSFER')


class OrderDirection(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ASC', 'DESC')


class OrgAddMemberAuditEntryPermission(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('READ', 'ADMIN')


class OrgCreateAuditEntryBillingPlan(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('FREE', 'BUSINESS', 'BUSINESS_PLUS', 'UNLIMITED', 'TIERED_PER_SEAT')


class OrgRemoveBillingManagerAuditEntryReason(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE', 'SAML_EXTERNAL_IDENTITY_MISSING', 'SAML_SSO_ENFORCEMENT_REQUIRES_EXTERNAL_IDENTITY')


class OrgRemoveMemberAuditEntryMembershipType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('DIRECT_MEMBER', 'ADMIN', 'BILLING_MANAGER', 'UNAFFILIATED', 'OUTSIDE_COLLABORATOR')


class OrgRemoveMemberAuditEntryReason(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE', 'SAML_EXTERNAL_IDENTITY_MISSING', 'SAML_SSO_ENFORCEMENT_REQUIRES_EXTERNAL_IDENTITY')


class OrgRemoveOutsideCollaboratorAuditEntryMembershipType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OUTSIDE_COLLABORATOR', 'UNAFFILIATED', 'BILLING_MANAGER')


class OrgRemoveOutsideCollaboratorAuditEntryReason(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('TWO_FACTOR_REQUIREMENT_NON_COMPLIANCE', 'SAML_EXTERNAL_IDENTITY_MISSING')


class OrgUpdateDefaultRepositoryPermissionAuditEntryPermission(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('READ', 'WRITE', 'ADMIN', 'NONE')


class OrgUpdateMemberAuditEntryPermission(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('READ', 'ADMIN')


class OrgUpdateMemberRepositoryCreationPermissionAuditEntryVisibility(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ALL', 'PUBLIC')


class OrganizationInvitationRole(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('DIRECT_MEMBER', 'ADMIN', 'BILLING_MANAGER', 'REINSTATE')


class OrganizationInvitationType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('USER', 'EMAIL')


class OrganizationMemberRole(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('MEMBER', 'ADMIN')


class OrganizationMembersCanCreateRepositoriesSettingValue(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ALL', 'PRIVATE', 'DISABLED')


class OrganizationOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'LOGIN')


class PinnableItemType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('REPOSITORY', 'GIST', 'ISSUE', 'PROJECT', 'PULL_REQUEST', 'USER', 'ORGANIZATION', 'TEAM')


class PreciseDateTime(sgqlc.types.Scalar):
    __schema__ = github_schema


class ProjectCardArchivedState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ARCHIVED', 'NOT_ARCHIVED')


class ProjectCardState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CONTENT_ONLY', 'NOTE_ONLY', 'REDACTED')


class ProjectColumnPurpose(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('TODO', 'IN_PROGRESS', 'DONE')


class ProjectOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'UPDATED_AT', 'NAME')


class ProjectState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OPEN', 'CLOSED')


class ProjectTemplate(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('BASIC_KANBAN', 'AUTOMATED_KANBAN_V2', 'AUTOMATED_REVIEWS_KANBAN', 'BUG_TRIAGE')


class PullRequestMergeMethod(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('MERGE', 'SQUASH', 'REBASE')


class PullRequestOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'UPDATED_AT')


class PullRequestPubSubTopic(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('UPDATED', 'MARKASREAD', 'HEAD_REF', 'TIMELINE', 'STATE')


class PullRequestReviewCommentState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('PENDING', 'SUBMITTED')


class PullRequestReviewEvent(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('COMMENT', 'APPROVE', 'REQUEST_CHANGES', 'DISMISS')


class PullRequestReviewState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('PENDING', 'COMMENTED', 'APPROVED', 'CHANGES_REQUESTED', 'DISMISSED')


class PullRequestState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OPEN', 'CLOSED', 'MERGED')


class PullRequestTimelineItemsItemType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('PULL_REQUEST_COMMIT', 'PULL_REQUEST_COMMIT_COMMENT_THREAD', 'PULL_REQUEST_REVIEW', 'PULL_REQUEST_REVIEW_THREAD', 'PULL_REQUEST_REVISION_MARKER', 'BASE_REF_CHANGED_EVENT', 'BASE_REF_FORCE_PUSHED_EVENT', 'DEPLOYED_EVENT', 'DEPLOYMENT_ENVIRONMENT_CHANGED_EVENT', 'HEAD_REF_DELETED_EVENT', 'HEAD_REF_FORCE_PUSHED_EVENT', 'HEAD_REF_RESTORED_EVENT', 'MERGED_EVENT', 'REVIEW_DISMISSED_EVENT', 'REVIEW_REQUESTED_EVENT', 'REVIEW_REQUEST_REMOVED_EVENT', 'READY_FOR_REVIEW_EVENT', 'ISSUE_COMMENT', 'CROSS_REFERENCED_EVENT', 'ADDED_TO_PROJECT_EVENT', 'ASSIGNED_EVENT', 'CLOSED_EVENT', 'COMMENT_DELETED_EVENT', 'CONVERTED_NOTE_TO_ISSUE_EVENT', 'DEMILESTONED_EVENT', 'LABELED_EVENT', 'LOCKED_EVENT', 'MARKED_AS_DUPLICATE_EVENT', 'MENTIONED_EVENT', 'MILESTONED_EVENT', 'MOVED_COLUMNS_IN_PROJECT_EVENT', 'PINNED_EVENT', 'REFERENCED_EVENT', 'REMOVED_FROM_PROJECT_EVENT', 'RENAMED_TITLE_EVENT', 'REOPENED_EVENT', 'SUBSCRIBED_EVENT', 'TRANSFERRED_EVENT', 'UNASSIGNED_EVENT', 'UNLABELED_EVENT', 'UNLOCKED_EVENT', 'USER_BLOCKED_EVENT', 'UNPINNED_EVENT', 'UNSUBSCRIBED_EVENT')


class PullRequestUpdateState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OPEN', 'CLOSED')


class ReactionContent(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('THUMBS_UP', 'THUMBS_DOWN', 'LAUGH', 'HOORAY', 'CONFUSED', 'HEART', 'ROCKET', 'EYES')


class ReactionOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT',)


class RefOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('TAG_COMMIT_DATE', 'ALPHABETICAL')


class RegistryPackageDependencyType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('DEFAULT', 'DEV', 'TEST', 'PEER', 'OPTIONAL', 'BUNDLED')


class RegistryPackageFileState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('NEW', 'UPLOADED')


class RegistryPackageType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('NPM', 'RUBYGEMS', 'MAVEN', 'DOCKER', 'DEBIAN', 'NUGET', 'PYTHON')


class ReleaseOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'NAME')


class RepoAccessAuditEntryVisibility(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('INTERNAL', 'PRIVATE', 'PUBLIC')


class RepoAddMemberAuditEntryVisibility(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('INTERNAL', 'PRIVATE', 'PUBLIC')


class RepoArchivedAuditEntryVisibility(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('INTERNAL', 'PRIVATE', 'PUBLIC')


class RepoChangeMergeSettingAuditEntryMergeType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('MERGE', 'REBASE', 'SQUASH')


class RepoCreateAuditEntryVisibility(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('INTERNAL', 'PRIVATE', 'PUBLIC')


class RepoDestroyAuditEntryVisibility(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('INTERNAL', 'PRIVATE', 'PUBLIC')


class RepoRemoveMemberAuditEntryVisibility(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('INTERNAL', 'PRIVATE', 'PUBLIC')


class ReportedContentClassifiers(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('SPAM', 'ABUSE', 'OFF_TOPIC', 'OUTDATED', 'RESOLVED')


class RepositoryAffiliation(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('OWNER', 'COLLABORATOR', 'ORGANIZATION_MEMBER')


class RepositoryCollaboratorAffiliation(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ALL', 'OUTSIDE')


class RepositoryContributionType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('COMMIT', 'ISSUE', 'PULL_REQUEST', 'REPOSITORY', 'PULL_REQUEST_REVIEW')


class RepositoryInvitationOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'INVITEE_LOGIN')


class RepositoryLockReason(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('MOVING', 'BILLING', 'RENAME', 'MIGRATING')


class RepositoryOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'UPDATED_AT', 'PUSHED_AT', 'NAME', 'STARGAZERS')


class RepositoryPermission(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ADMIN', 'MAINTAIN', 'WRITE', 'TRIAGE', 'READ')


class RepositoryPrivacy(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('PUBLIC', 'PRIVATE')


class RepositoryVisibility(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('PRIVATE', 'PUBLIC', 'INTERNAL')


class SamlDigestAlgorithm(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('SHA1', 'SHA256', 'SHA384', 'SHA512')


class SamlSignatureAlgorithm(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('RSA_SHA1', 'RSA_SHA256', 'RSA_SHA384', 'RSA_SHA512')


class SavedReplyOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('UPDATED_AT',)


class SearchType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ISSUE', 'REPOSITORY', 'USER')


class SecurityAdvisoryEcosystem(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('RUBYGEMS', 'NPM', 'PIP', 'MAVEN', 'NUGET', 'COMPOSER')


class SecurityAdvisoryIdentifierType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CVE', 'GHSA')


class SecurityAdvisoryOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('PUBLISHED_AT', 'UPDATED_AT')


class SecurityAdvisorySeverity(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('LOW', 'MODERATE', 'HIGH', 'CRITICAL')


class SecurityVulnerabilityOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('UPDATED_AT',)


class SponsorsTierOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'MONTHLY_PRICE_IN_CENTS')


class SponsorshipOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT',)


class SponsorshipPrivacy(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('PUBLIC', 'PRIVATE')


class StarOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('STARRED_AT',)


class StatusState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('EXPECTED', 'ERROR', 'FAILURE', 'PENDING', 'SUCCESS')


String = sgqlc.types.String

class SubscriptionState(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('UNSUBSCRIBED', 'SUBSCRIBED', 'IGNORED')


class TeamDiscussionCommentOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('NUMBER',)


class TeamDiscussionOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT',)


class TeamMemberOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('LOGIN', 'CREATED_AT')


class TeamMemberRole(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('MAINTAINER', 'MEMBER')


class TeamMembershipType(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('IMMEDIATE', 'CHILD_TEAM', 'ALL')


class TeamOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('NAME',)


class TeamPrivacy(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('SECRET', 'VISIBLE')


class TeamRepositoryOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('CREATED_AT', 'UPDATED_AT', 'PUSHED_AT', 'NAME', 'PERMISSION', 'STARGAZERS')


class TeamRole(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ADMIN', 'MEMBER')


class TopicSuggestionDeclineReason(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('NOT_RELEVANT', 'TOO_SPECIFIC', 'PERSONAL_PREFERENCE', 'TOO_GENERAL')


class URI(sgqlc.types.Scalar):
    __schema__ = github_schema


class UserBlockDuration(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('ONE_DAY', 'THREE_DAYS', 'ONE_WEEK', 'ONE_MONTH', 'PERMANENT')


class UserStatusOrderField(sgqlc.types.Enum):
    __schema__ = github_schema
    __choices__ = ('UPDATED_AT',)


class X509Certificate(sgqlc.types.Scalar):
    __schema__ = github_schema



########################################################################
# Input Objects
########################################################################
class AcceptEnterpriseAdministratorInvitationInput(sgqlc.types.Input):
    __schema__ = github_schema
    invitation_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='invitationId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class AcceptTopicSuggestionInput(sgqlc.types.Input):
    __schema__ = github_schema
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class AddAssigneesToAssignableInput(sgqlc.types.Input):
    __schema__ = github_schema
    assignable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='assignableId')
    assignee_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='assigneeIds')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class AddCommentInput(sgqlc.types.Input):
    __schema__ = github_schema
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class AddLabelsToLabelableInput(sgqlc.types.Input):
    __schema__ = github_schema
    labelable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='labelableId')
    label_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='labelIds')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class AddProjectCardInput(sgqlc.types.Input):
    __schema__ = github_schema
    project_column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectColumnId')
    content_id = sgqlc.types.Field(ID, graphql_name='contentId')
    note = sgqlc.types.Field(String, graphql_name='note')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class AddProjectColumnInput(sgqlc.types.Input):
    __schema__ = github_schema
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class AddPullRequestReviewCommentInput(sgqlc.types.Input):
    __schema__ = github_schema
    pull_request_review_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewId')
    commit_oid = sgqlc.types.Field(GitObjectID, graphql_name='commitOID')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    path = sgqlc.types.Field(String, graphql_name='path')
    position = sgqlc.types.Field(Int, graphql_name='position')
    in_reply_to = sgqlc.types.Field(ID, graphql_name='inReplyTo')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class AddPullRequestReviewInput(sgqlc.types.Input):
    __schema__ = github_schema
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    commit_oid = sgqlc.types.Field(GitObjectID, graphql_name='commitOID')
    body = sgqlc.types.Field(String, graphql_name='body')
    event = sgqlc.types.Field(PullRequestReviewEvent, graphql_name='event')
    comments = sgqlc.types.Field(sgqlc.types.list_of('DraftPullRequestReviewComment'), graphql_name='comments')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class AddReactionInput(sgqlc.types.Input):
    __schema__ = github_schema
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')
    content = sgqlc.types.Field(sgqlc.types.non_null(ReactionContent), graphql_name='content')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class AddStarInput(sgqlc.types.Input):
    __schema__ = github_schema
    starrable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='starrableId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ArchiveRepositoryInput(sgqlc.types.Input):
    __schema__ = github_schema
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class AuditLogOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(AuditLogOrderField, graphql_name='field')
    direction = sgqlc.types.Field(OrderDirection, graphql_name='direction')


class CancelEnterpriseAdminInvitationInput(sgqlc.types.Input):
    __schema__ = github_schema
    invitation_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='invitationId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ChangeUserStatusInput(sgqlc.types.Input):
    __schema__ = github_schema
    emoji = sgqlc.types.Field(String, graphql_name='emoji')
    message = sgqlc.types.Field(String, graphql_name='message')
    organization_id = sgqlc.types.Field(ID, graphql_name='organizationId')
    limited_availability = sgqlc.types.Field(Boolean, graphql_name='limitedAvailability')
    expires_at = sgqlc.types.Field(DateTime, graphql_name='expiresAt')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ClearLabelsFromLabelableInput(sgqlc.types.Input):
    __schema__ = github_schema
    labelable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='labelableId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CloneProjectInput(sgqlc.types.Input):
    __schema__ = github_schema
    target_owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='targetOwnerId')
    source_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='sourceId')
    include_workflows = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includeWorkflows')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    body = sgqlc.types.Field(String, graphql_name='body')
    public = sgqlc.types.Field(Boolean, graphql_name='public')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CloneTemplateRepositoryInput(sgqlc.types.Input):
    __schema__ = github_schema
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    description = sgqlc.types.Field(String, graphql_name='description')
    visibility = sgqlc.types.Field(sgqlc.types.non_null(RepositoryVisibility), graphql_name='visibility')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CloseIssueInput(sgqlc.types.Input):
    __schema__ = github_schema
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ClosePullRequestInput(sgqlc.types.Input):
    __schema__ = github_schema
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CommitAuthor(sgqlc.types.Input):
    __schema__ = github_schema
    id = sgqlc.types.Field(ID, graphql_name='id')
    emails = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='emails')


class CommitContributionOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(CommitContributionOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ContributionOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(ContributionOrderField, graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ConvertProjectCardNoteToIssueInput(sgqlc.types.Input):
    __schema__ = github_schema
    project_card_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectCardId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    title = sgqlc.types.Field(String, graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateBranchProtectionRuleInput(sgqlc.types.Input):
    __schema__ = github_schema
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')
    requires_approving_reviews = sgqlc.types.Field(Boolean, graphql_name='requiresApprovingReviews')
    required_approving_review_count = sgqlc.types.Field(Int, graphql_name='requiredApprovingReviewCount')
    requires_commit_signatures = sgqlc.types.Field(Boolean, graphql_name='requiresCommitSignatures')
    is_admin_enforced = sgqlc.types.Field(Boolean, graphql_name='isAdminEnforced')
    requires_status_checks = sgqlc.types.Field(Boolean, graphql_name='requiresStatusChecks')
    requires_strict_status_checks = sgqlc.types.Field(Boolean, graphql_name='requiresStrictStatusChecks')
    requires_code_owner_reviews = sgqlc.types.Field(Boolean, graphql_name='requiresCodeOwnerReviews')
    dismisses_stale_reviews = sgqlc.types.Field(Boolean, graphql_name='dismissesStaleReviews')
    restricts_review_dismissals = sgqlc.types.Field(Boolean, graphql_name='restrictsReviewDismissals')
    review_dismissal_actor_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='reviewDismissalActorIds')
    restricts_pushes = sgqlc.types.Field(Boolean, graphql_name='restrictsPushes')
    push_actor_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='pushActorIds')
    required_status_check_contexts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='requiredStatusCheckContexts')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateContentAttachmentInput(sgqlc.types.Input):
    __schema__ = github_schema
    content_reference_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='contentReferenceId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateEnterpriseOrganizationInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    profile_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='profileName')
    billing_email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='billingEmail')
    admin_logins = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='adminLogins')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateIssueInput(sgqlc.types.Input):
    __schema__ = github_schema
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    assignee_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='assigneeIds')
    milestone_id = sgqlc.types.Field(ID, graphql_name='milestoneId')
    label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='labelIds')
    project_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='projectIds')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateProjectInput(sgqlc.types.Input):
    __schema__ = github_schema
    owner_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='ownerId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    body = sgqlc.types.Field(String, graphql_name='body')
    template = sgqlc.types.Field(ProjectTemplate, graphql_name='template')
    repository_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='repositoryIds')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreatePullRequestInput(sgqlc.types.Input):
    __schema__ = github_schema
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    base_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='baseRefName')
    head_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='headRefName')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    maintainer_can_modify = sgqlc.types.Field(Boolean, graphql_name='maintainerCanModify')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateRefInput(sgqlc.types.Input):
    __schema__ = github_schema
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateRepositoryInput(sgqlc.types.Input):
    __schema__ = github_schema
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    owner_id = sgqlc.types.Field(ID, graphql_name='ownerId')
    description = sgqlc.types.Field(String, graphql_name='description')
    visibility = sgqlc.types.Field(sgqlc.types.non_null(RepositoryVisibility), graphql_name='visibility')
    template = sgqlc.types.Field(Boolean, graphql_name='template')
    homepage_url = sgqlc.types.Field(URI, graphql_name='homepageUrl')
    has_wiki_enabled = sgqlc.types.Field(Boolean, graphql_name='hasWikiEnabled')
    has_issues_enabled = sgqlc.types.Field(Boolean, graphql_name='hasIssuesEnabled')
    team_id = sgqlc.types.Field(ID, graphql_name='teamId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateTeamDiscussionCommentInput(sgqlc.types.Input):
    __schema__ = github_schema
    discussion_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='discussionId')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateTeamDiscussionInput(sgqlc.types.Input):
    __schema__ = github_schema
    team_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='teamId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    private = sgqlc.types.Field(Boolean, graphql_name='private')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeclineTopicSuggestionInput(sgqlc.types.Input):
    __schema__ = github_schema
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    reason = sgqlc.types.Field(sgqlc.types.non_null(TopicSuggestionDeclineReason), graphql_name='reason')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteBranchProtectionRuleInput(sgqlc.types.Input):
    __schema__ = github_schema
    branch_protection_rule_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='branchProtectionRuleId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteIssueCommentInput(sgqlc.types.Input):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteIssueInput(sgqlc.types.Input):
    __schema__ = github_schema
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeletePackageVersionInput(sgqlc.types.Input):
    __schema__ = github_schema
    package_version_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='packageVersionId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteProjectCardInput(sgqlc.types.Input):
    __schema__ = github_schema
    card_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cardId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteProjectColumnInput(sgqlc.types.Input):
    __schema__ = github_schema
    column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='columnId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteProjectInput(sgqlc.types.Input):
    __schema__ = github_schema
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeletePullRequestReviewCommentInput(sgqlc.types.Input):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeletePullRequestReviewInput(sgqlc.types.Input):
    __schema__ = github_schema
    pull_request_review_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteRefInput(sgqlc.types.Input):
    __schema__ = github_schema
    ref_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='refId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteTeamDiscussionCommentInput(sgqlc.types.Input):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteTeamDiscussionInput(sgqlc.types.Input):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeploymentOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(DeploymentOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class DismissPullRequestReviewInput(sgqlc.types.Input):
    __schema__ = github_schema
    pull_request_review_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewId')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DraftPullRequestReviewComment(sgqlc.types.Input):
    __schema__ = github_schema
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')


class EnterpriseAdministratorInvitationOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseAdministratorInvitationOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class EnterpriseMemberOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseMemberOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class EnterpriseOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class EnterpriseServerInstallationOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerInstallationOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class EnterpriseServerUserAccountEmailOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccountEmailOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class EnterpriseServerUserAccountOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccountOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class EnterpriseServerUserAccountsUploadOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccountsUploadOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class FollowUserInput(sgqlc.types.Input):
    __schema__ = github_schema
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='userId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class GistOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(GistOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ImportProjectInput(sgqlc.types.Input):
    __schema__ = github_schema
    owner_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ownerName')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    body = sgqlc.types.Field(String, graphql_name='body')
    public = sgqlc.types.Field(Boolean, graphql_name='public')
    column_imports = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProjectColumnImport'))), graphql_name='columnImports')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class InviteEnterpriseAdminInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    invitee = sgqlc.types.Field(String, graphql_name='invitee')
    email = sgqlc.types.Field(String, graphql_name='email')
    role = sgqlc.types.Field(EnterpriseAdministratorRole, graphql_name='role')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class IssueFilters(sgqlc.types.Input):
    __schema__ = github_schema
    assignee = sgqlc.types.Field(String, graphql_name='assignee')
    created_by = sgqlc.types.Field(String, graphql_name='createdBy')
    labels = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels')
    mentioned = sgqlc.types.Field(String, graphql_name='mentioned')
    milestone = sgqlc.types.Field(String, graphql_name='milestone')
    since = sgqlc.types.Field(DateTime, graphql_name='since')
    states = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='states')
    viewer_subscribed = sgqlc.types.Field(Boolean, graphql_name='viewerSubscribed')


class IssueOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(IssueOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class LanguageOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(LanguageOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class LinkRepositoryToProjectInput(sgqlc.types.Input):
    __schema__ = github_schema
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class LockLockableInput(sgqlc.types.Input):
    __schema__ = github_schema
    lockable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='lockableId')
    lock_reason = sgqlc.types.Field(LockReason, graphql_name='lockReason')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class MergeBranchInput(sgqlc.types.Input):
    __schema__ = github_schema
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    base = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='base')
    head = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='head')
    commit_message = sgqlc.types.Field(String, graphql_name='commitMessage')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class MergePullRequestInput(sgqlc.types.Input):
    __schema__ = github_schema
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    commit_headline = sgqlc.types.Field(String, graphql_name='commitHeadline')
    commit_body = sgqlc.types.Field(String, graphql_name='commitBody')
    expected_head_oid = sgqlc.types.Field(GitObjectID, graphql_name='expectedHeadOid')
    merge_method = sgqlc.types.Field(PullRequestMergeMethod, graphql_name='mergeMethod')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class MilestoneOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(MilestoneOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class MinimizeCommentInput(sgqlc.types.Input):
    __schema__ = github_schema
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')
    classifier = sgqlc.types.Field(sgqlc.types.non_null(ReportedContentClassifiers), graphql_name='classifier')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class MoveProjectCardInput(sgqlc.types.Input):
    __schema__ = github_schema
    card_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='cardId')
    column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='columnId')
    after_card_id = sgqlc.types.Field(ID, graphql_name='afterCardId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class MoveProjectColumnInput(sgqlc.types.Input):
    __schema__ = github_schema
    column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='columnId')
    after_column_id = sgqlc.types.Field(ID, graphql_name='afterColumnId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class OrganizationOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(OrganizationOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class PinIssueInput(sgqlc.types.Input):
    __schema__ = github_schema
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ProjectCardImport(sgqlc.types.Input):
    __schema__ = github_schema
    repository = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='repository')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')


class ProjectColumnImport(sgqlc.types.Input):
    __schema__ = github_schema
    column_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='columnName')
    position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='position')
    issues = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ProjectCardImport)), graphql_name='issues')


class ProjectOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(ProjectOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class PullRequestOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(PullRequestOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class ReactionOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(ReactionOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class RefOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(RefOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class RegenerateEnterpriseIdentityProviderRecoveryCodesInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class RegistryPackageMetadatum(sgqlc.types.Input):
    __schema__ = github_schema
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')
    update = sgqlc.types.Field(Boolean, graphql_name='update')


class ReleaseOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(ReleaseOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class RemoveAssigneesFromAssignableInput(sgqlc.types.Input):
    __schema__ = github_schema
    assignable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='assignableId')
    assignee_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='assigneeIds')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class RemoveEnterpriseAdminInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class RemoveEnterpriseOrganizationInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class RemoveLabelsFromLabelableInput(sgqlc.types.Input):
    __schema__ = github_schema
    labelable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='labelableId')
    label_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='labelIds')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class RemoveOutsideCollaboratorInput(sgqlc.types.Input):
    __schema__ = github_schema
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='userId')
    organization_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='organizationId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class RemoveReactionInput(sgqlc.types.Input):
    __schema__ = github_schema
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')
    content = sgqlc.types.Field(sgqlc.types.non_null(ReactionContent), graphql_name='content')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class RemoveStarInput(sgqlc.types.Input):
    __schema__ = github_schema
    starrable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='starrableId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ReopenIssueInput(sgqlc.types.Input):
    __schema__ = github_schema
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ReopenPullRequestInput(sgqlc.types.Input):
    __schema__ = github_schema
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class RepositoryInvitationOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(RepositoryInvitationOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class RepositoryOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(RepositoryOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class RequestReviewsInput(sgqlc.types.Input):
    __schema__ = github_schema
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    user_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='userIds')
    team_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='teamIds')
    union = sgqlc.types.Field(Boolean, graphql_name='union')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ResolveReviewThreadInput(sgqlc.types.Input):
    __schema__ = github_schema
    thread_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='threadId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class SavedReplyOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(SavedReplyOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class SecurityAdvisoryIdentifierFilter(sgqlc.types.Input):
    __schema__ = github_schema
    type = sgqlc.types.Field(sgqlc.types.non_null(SecurityAdvisoryIdentifierType), graphql_name='type')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class SecurityAdvisoryOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(SecurityAdvisoryOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class SecurityVulnerabilityOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(SecurityVulnerabilityOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class SponsorsTierOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(SponsorsTierOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class SponsorshipOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(SponsorshipOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class StarOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(StarOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class SubmitPullRequestReviewInput(sgqlc.types.Input):
    __schema__ = github_schema
    pull_request_review_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewId')
    event = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewEvent), graphql_name='event')
    body = sgqlc.types.Field(String, graphql_name='body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class TeamDiscussionCommentOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(TeamDiscussionCommentOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class TeamDiscussionOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(TeamDiscussionOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class TeamMemberOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(TeamMemberOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class TeamOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(TeamOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class TeamRepositoryOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(TeamRepositoryOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')


class TransferIssueInput(sgqlc.types.Input):
    __schema__ = github_schema
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UnarchiveRepositoryInput(sgqlc.types.Input):
    __schema__ = github_schema
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UnfollowUserInput(sgqlc.types.Input):
    __schema__ = github_schema
    user_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='userId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UnlinkRepositoryFromProjectInput(sgqlc.types.Input):
    __schema__ = github_schema
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UnlockLockableInput(sgqlc.types.Input):
    __schema__ = github_schema
    lockable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='lockableId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UnmarkIssueAsDuplicateInput(sgqlc.types.Input):
    __schema__ = github_schema
    duplicate_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='duplicateId')
    canonical_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='canonicalId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UnminimizeCommentInput(sgqlc.types.Input):
    __schema__ = github_schema
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subjectId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UnpinIssueInput(sgqlc.types.Input):
    __schema__ = github_schema
    issue_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='issueId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UnresolveReviewThreadInput(sgqlc.types.Input):
    __schema__ = github_schema
    thread_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='threadId')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateBranchProtectionRuleInput(sgqlc.types.Input):
    __schema__ = github_schema
    branch_protection_rule_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='branchProtectionRuleId')
    pattern = sgqlc.types.Field(String, graphql_name='pattern')
    requires_approving_reviews = sgqlc.types.Field(Boolean, graphql_name='requiresApprovingReviews')
    required_approving_review_count = sgqlc.types.Field(Int, graphql_name='requiredApprovingReviewCount')
    requires_commit_signatures = sgqlc.types.Field(Boolean, graphql_name='requiresCommitSignatures')
    is_admin_enforced = sgqlc.types.Field(Boolean, graphql_name='isAdminEnforced')
    requires_status_checks = sgqlc.types.Field(Boolean, graphql_name='requiresStatusChecks')
    requires_strict_status_checks = sgqlc.types.Field(Boolean, graphql_name='requiresStrictStatusChecks')
    requires_code_owner_reviews = sgqlc.types.Field(Boolean, graphql_name='requiresCodeOwnerReviews')
    dismisses_stale_reviews = sgqlc.types.Field(Boolean, graphql_name='dismissesStaleReviews')
    restricts_review_dismissals = sgqlc.types.Field(Boolean, graphql_name='restrictsReviewDismissals')
    review_dismissal_actor_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='reviewDismissalActorIds')
    restricts_pushes = sgqlc.types.Field(Boolean, graphql_name='restrictsPushes')
    push_actor_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='pushActorIds')
    required_status_check_contexts = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='requiredStatusCheckContexts')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseActionExecutionCapabilitySettingInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    capability = sgqlc.types.Field(sgqlc.types.non_null(ActionExecutionCapabilitySetting), graphql_name='capability')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseAdministratorRoleInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    role = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseAdministratorRole), graphql_name='role')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseDefaultRepositoryPermissionSettingInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseDefaultRepositoryPermissionSettingValue), graphql_name='settingValue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseMembersCanCreateRepositoriesSettingInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(EnterpriseMembersCanCreateRepositoriesSettingValue, graphql_name='settingValue')
    members_can_create_repositories_policy_enabled = sgqlc.types.Field(Boolean, graphql_name='membersCanCreateRepositoriesPolicyEnabled')
    members_can_create_public_repositories = sgqlc.types.Field(Boolean, graphql_name='membersCanCreatePublicRepositories')
    members_can_create_private_repositories = sgqlc.types.Field(Boolean, graphql_name='membersCanCreatePrivateRepositories')
    members_can_create_internal_repositories = sgqlc.types.Field(Boolean, graphql_name='membersCanCreateInternalRepositories')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseMembersCanDeleteIssuesSettingInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseMembersCanMakePurchasesSettingInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseMembersCanMakePurchasesSettingValue), graphql_name='settingValue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseOrganizationProjectsSettingInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseProfileInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    website_url = sgqlc.types.Field(String, graphql_name='websiteUrl')
    location = sgqlc.types.Field(String, graphql_name='location')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseRepositoryProjectsSettingInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseTeamDiscussionsSettingInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='settingValue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput(sgqlc.types.Input):
    __schema__ = github_schema
    enterprise_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='enterpriseId')
    setting_value = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledSettingValue), graphql_name='settingValue')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateIssueCommentInput(sgqlc.types.Input):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateIssueInput(sgqlc.types.Input):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    assignee_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='assigneeIds')
    milestone_id = sgqlc.types.Field(ID, graphql_name='milestoneId')
    label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='labelIds')
    state = sgqlc.types.Field(IssueState, graphql_name='state')
    project_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='projectIds')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateProjectCardInput(sgqlc.types.Input):
    __schema__ = github_schema
    project_card_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectCardId')
    is_archived = sgqlc.types.Field(Boolean, graphql_name='isArchived')
    note = sgqlc.types.Field(String, graphql_name='note')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateProjectColumnInput(sgqlc.types.Input):
    __schema__ = github_schema
    project_column_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectColumnId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateProjectInput(sgqlc.types.Input):
    __schema__ = github_schema
    project_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='projectId')
    name = sgqlc.types.Field(String, graphql_name='name')
    body = sgqlc.types.Field(String, graphql_name='body')
    state = sgqlc.types.Field(ProjectState, graphql_name='state')
    public = sgqlc.types.Field(Boolean, graphql_name='public')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdatePullRequestInput(sgqlc.types.Input):
    __schema__ = github_schema
    pull_request_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestId')
    base_ref_name = sgqlc.types.Field(String, graphql_name='baseRefName')
    title = sgqlc.types.Field(String, graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    state = sgqlc.types.Field(PullRequestUpdateState, graphql_name='state')
    maintainer_can_modify = sgqlc.types.Field(Boolean, graphql_name='maintainerCanModify')
    assignee_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='assigneeIds')
    milestone_id = sgqlc.types.Field(ID, graphql_name='milestoneId')
    label_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='labelIds')
    project_ids = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ID)), graphql_name='projectIds')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdatePullRequestReviewCommentInput(sgqlc.types.Input):
    __schema__ = github_schema
    pull_request_review_comment_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewCommentId')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdatePullRequestReviewInput(sgqlc.types.Input):
    __schema__ = github_schema
    pull_request_review_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='pullRequestReviewId')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateRefInput(sgqlc.types.Input):
    __schema__ = github_schema
    ref_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='refId')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    force = sgqlc.types.Field(Boolean, graphql_name='force')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateRepositoryInput(sgqlc.types.Input):
    __schema__ = github_schema
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    template = sgqlc.types.Field(Boolean, graphql_name='template')
    homepage_url = sgqlc.types.Field(URI, graphql_name='homepageUrl')
    has_wiki_enabled = sgqlc.types.Field(Boolean, graphql_name='hasWikiEnabled')
    has_issues_enabled = sgqlc.types.Field(Boolean, graphql_name='hasIssuesEnabled')
    has_projects_enabled = sgqlc.types.Field(Boolean, graphql_name='hasProjectsEnabled')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateSubscriptionInput(sgqlc.types.Input):
    __schema__ = github_schema
    subscribable_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='subscribableId')
    state = sgqlc.types.Field(sgqlc.types.non_null(SubscriptionState), graphql_name='state')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateTeamDiscussionCommentInput(sgqlc.types.Input):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_version = sgqlc.types.Field(String, graphql_name='bodyVersion')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateTeamDiscussionInput(sgqlc.types.Input):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')
    body = sgqlc.types.Field(String, graphql_name='body')
    body_version = sgqlc.types.Field(String, graphql_name='bodyVersion')
    pinned = sgqlc.types.Field(Boolean, graphql_name='pinned')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateTopicsInput(sgqlc.types.Input):
    __schema__ = github_schema
    repository_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='repositoryId')
    topic_names = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='topicNames')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UserStatusOrder(sgqlc.types.Input):
    __schema__ = github_schema
    field = sgqlc.types.Field(sgqlc.types.non_null(UserStatusOrderField), graphql_name='field')
    direction = sgqlc.types.Field(sgqlc.types.non_null(OrderDirection), graphql_name='direction')



########################################################################
# Output Objects and Interfaces
########################################################################
class AcceptEnterpriseAdministratorInvitationPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invitation = sgqlc.types.Field('EnterpriseAdministratorInvitation', graphql_name='invitation')
    message = sgqlc.types.Field(String, graphql_name='message')


class AcceptTopicSuggestionPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    topic = sgqlc.types.Field('Topic', graphql_name='topic')


class Actor(sgqlc.types.Interface):
    __schema__ = github_schema
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class ActorLocation(sgqlc.types.Type):
    __schema__ = github_schema
    city = sgqlc.types.Field(String, graphql_name='city')
    country = sgqlc.types.Field(String, graphql_name='country')
    country_code = sgqlc.types.Field(String, graphql_name='countryCode')
    region = sgqlc.types.Field(String, graphql_name='region')
    region_code = sgqlc.types.Field(String, graphql_name='regionCode')


class AddAssigneesToAssignablePayload(sgqlc.types.Type):
    __schema__ = github_schema
    assignable = sgqlc.types.Field('Assignable', graphql_name='assignable')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class AddCommentPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment_edge = sgqlc.types.Field('IssueCommentEdge', graphql_name='commentEdge')
    subject = sgqlc.types.Field('Node', graphql_name='subject')
    timeline_edge = sgqlc.types.Field('IssueTimelineItemEdge', graphql_name='timelineEdge')


class AddLabelsToLabelablePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    labelable = sgqlc.types.Field('Labelable', graphql_name='labelable')


class AddProjectCardPayload(sgqlc.types.Type):
    __schema__ = github_schema
    card_edge = sgqlc.types.Field('ProjectCardEdge', graphql_name='cardEdge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_column = sgqlc.types.Field('ProjectColumn', graphql_name='projectColumn')


class AddProjectColumnPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    column_edge = sgqlc.types.Field('ProjectColumnEdge', graphql_name='columnEdge')
    project = sgqlc.types.Field('Project', graphql_name='project')


class AddPullRequestReviewCommentPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    comment = sgqlc.types.Field('PullRequestReviewComment', graphql_name='comment')
    comment_edge = sgqlc.types.Field('PullRequestReviewCommentEdge', graphql_name='commentEdge')


class AddPullRequestReviewPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field('PullRequestReview', graphql_name='pullRequestReview')
    review_edge = sgqlc.types.Field('PullRequestReviewEdge', graphql_name='reviewEdge')


class AddReactionPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    reaction = sgqlc.types.Field('Reaction', graphql_name='reaction')
    subject = sgqlc.types.Field('Reactable', graphql_name='subject')


class AddStarPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    starrable = sgqlc.types.Field('Starrable', graphql_name='starrable')


class AppEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('App', graphql_name='node')


class ArchiveRepositoryPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class Assignable(sgqlc.types.Interface):
    __schema__ = github_schema
    assignees = sgqlc.types.Field(sgqlc.types.non_null('UserConnection'), graphql_name='assignees', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class AuditEntry(sgqlc.types.Interface):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class Blame(sgqlc.types.Type):
    __schema__ = github_schema
    ranges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BlameRange'))), graphql_name='ranges')


class BlameRange(sgqlc.types.Type):
    __schema__ = github_schema
    age = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='age')
    commit = sgqlc.types.Field(sgqlc.types.non_null('Commit'), graphql_name='commit')
    ending_line = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='endingLine')
    starting_line = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='startingLine')


class BranchProtectionRuleConflict(sgqlc.types.Type):
    __schema__ = github_schema
    branch_protection_rule = sgqlc.types.Field('BranchProtectionRule', graphql_name='branchProtectionRule')
    conflicting_branch_protection_rule = sgqlc.types.Field('BranchProtectionRule', graphql_name='conflictingBranchProtectionRule')
    ref = sgqlc.types.Field('Ref', graphql_name='ref')


class BranchProtectionRuleConflictConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('BranchProtectionRuleConflictEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(BranchProtectionRuleConflict), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class BranchProtectionRuleConflictEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(BranchProtectionRuleConflict, graphql_name='node')


class BranchProtectionRuleConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('BranchProtectionRuleEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('BranchProtectionRule'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class BranchProtectionRuleEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('BranchProtectionRule', graphql_name='node')


class CancelEnterpriseAdminInvitationPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invitation = sgqlc.types.Field('EnterpriseAdministratorInvitation', graphql_name='invitation')
    message = sgqlc.types.Field(String, graphql_name='message')


class ChangeUserStatusPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    status = sgqlc.types.Field('UserStatus', graphql_name='status')


class ClearLabelsFromLabelablePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    labelable = sgqlc.types.Field('Labelable', graphql_name='labelable')


class CloneProjectPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    job_status_id = sgqlc.types.Field(String, graphql_name='jobStatusId')
    project = sgqlc.types.Field('Project', graphql_name='project')


class CloneTemplateRepositoryPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class Closable(sgqlc.types.Interface):
    __schema__ = github_schema
    closed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='closed')
    closed_at = sgqlc.types.Field(DateTime, graphql_name='closedAt')


class CloseIssuePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class ClosePullRequestPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class Comment(sgqlc.types.Interface):
    __schema__ = github_schema
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    includes_created_edit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includesCreatedEdit')
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    user_content_edits = sgqlc.types.Field('UserContentEditConnection', graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')


class CommitCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('CommitCommentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CommitComment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CommitCommentEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CommitComment', graphql_name='node')


class CommitConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('CommitEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Commit'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CommitContributionsByRepository(sgqlc.types.Type):
    __schema__ = github_schema
    contributions = sgqlc.types.Field(sgqlc.types.non_null('CreatedCommitContributionConnection'), graphql_name='contributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(CommitContributionOrder, graphql_name='orderBy', default={'field': 'OCCURRED_AT', 'direction': 'DESC'})),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class CommitEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Commit', graphql_name='node')


class CommitHistoryConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of(CommitEdge), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Commit'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ContentAttachment(sgqlc.types.Type):
    __schema__ = github_schema
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    content_reference = sgqlc.types.Field(sgqlc.types.non_null('ContentReference'), graphql_name='contentReference')
    database_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class ContentReference(sgqlc.types.Type):
    __schema__ = github_schema
    database_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    reference = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='reference')


class Contribution(sgqlc.types.Interface):
    __schema__ = github_schema
    is_restricted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRestricted')
    occurred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='occurredAt')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')


class ContributionCalendar(sgqlc.types.Type):
    __schema__ = github_schema
    colors = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(String))), graphql_name='colors')
    is_halloween = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isHalloween')
    months = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ContributionCalendarMonth'))), graphql_name='months')
    total_contributions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalContributions')
    weeks = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ContributionCalendarWeek'))), graphql_name='weeks')


class ContributionCalendarDay(sgqlc.types.Type):
    __schema__ = github_schema
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    contribution_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='contributionCount')
    date = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='date')
    weekday = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='weekday')


class ContributionCalendarMonth(sgqlc.types.Type):
    __schema__ = github_schema
    first_day = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='firstDay')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    total_weeks = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalWeeks')
    year = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='year')


class ContributionCalendarWeek(sgqlc.types.Type):
    __schema__ = github_schema
    contribution_days = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ContributionCalendarDay))), graphql_name='contributionDays')
    first_day = sgqlc.types.Field(sgqlc.types.non_null(Date), graphql_name='firstDay')


class ContributionsCollection(sgqlc.types.Type):
    __schema__ = github_schema
    commit_contributions_by_repository = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommitContributionsByRepository))), graphql_name='commitContributionsByRepository', args=sgqlc.types.ArgDict((
        ('max_repositories', sgqlc.types.Arg(Int, graphql_name='maxRepositories', default=25)),
))
    )
    contribution_calendar = sgqlc.types.Field(sgqlc.types.non_null(ContributionCalendar), graphql_name='contributionCalendar')
    contribution_years = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='contributionYears')
    does_end_in_current_month = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='doesEndInCurrentMonth')
    earliest_restricted_contribution_date = sgqlc.types.Field(Date, graphql_name='earliestRestrictedContributionDate')
    ended_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='endedAt')
    first_issue_contribution = sgqlc.types.Field('CreatedIssueOrRestrictedContribution', graphql_name='firstIssueContribution')
    first_pull_request_contribution = sgqlc.types.Field('CreatedPullRequestOrRestrictedContribution', graphql_name='firstPullRequestContribution')
    first_repository_contribution = sgqlc.types.Field('CreatedRepositoryOrRestrictedContribution', graphql_name='firstRepositoryContribution')
    has_activity_in_the_past = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasActivityInThePast')
    has_any_contributions = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasAnyContributions')
    has_any_restricted_contributions = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasAnyRestrictedContributions')
    is_single_day = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSingleDay')
    issue_contributions = sgqlc.types.Field(sgqlc.types.non_null('CreatedIssueContributionConnection'), graphql_name='issueContributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
        ('order_by', sgqlc.types.Arg(ContributionOrder, graphql_name='orderBy', default={'field': 'OCCURRED_AT', 'direction': 'DESC'})),
))
    )
    issue_contributions_by_repository = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('IssueContributionsByRepository'))), graphql_name='issueContributionsByRepository', args=sgqlc.types.ArgDict((
        ('max_repositories', sgqlc.types.Arg(Int, graphql_name='maxRepositories', default=25)),
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
))
    )
    joined_git_hub_contribution = sgqlc.types.Field('JoinedGitHubContribution', graphql_name='joinedGitHubContribution')
    latest_restricted_contribution_date = sgqlc.types.Field(Date, graphql_name='latestRestrictedContributionDate')
    most_recent_collection_with_activity = sgqlc.types.Field('ContributionsCollection', graphql_name='mostRecentCollectionWithActivity')
    most_recent_collection_without_activity = sgqlc.types.Field('ContributionsCollection', graphql_name='mostRecentCollectionWithoutActivity')
    popular_issue_contribution = sgqlc.types.Field('CreatedIssueContribution', graphql_name='popularIssueContribution')
    popular_pull_request_contribution = sgqlc.types.Field('CreatedPullRequestContribution', graphql_name='popularPullRequestContribution')
    pull_request_contributions = sgqlc.types.Field(sgqlc.types.non_null('CreatedPullRequestContributionConnection'), graphql_name='pullRequestContributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
        ('order_by', sgqlc.types.Arg(ContributionOrder, graphql_name='orderBy', default={'field': 'OCCURRED_AT', 'direction': 'DESC'})),
))
    )
    pull_request_contributions_by_repository = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PullRequestContributionsByRepository'))), graphql_name='pullRequestContributionsByRepository', args=sgqlc.types.ArgDict((
        ('max_repositories', sgqlc.types.Arg(Int, graphql_name='maxRepositories', default=25)),
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
))
    )
    pull_request_review_contributions = sgqlc.types.Field(sgqlc.types.non_null('CreatedPullRequestReviewContributionConnection'), graphql_name='pullRequestReviewContributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ContributionOrder, graphql_name='orderBy', default={'field': 'OCCURRED_AT', 'direction': 'DESC'})),
))
    )
    pull_request_review_contributions_by_repository = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PullRequestReviewContributionsByRepository'))), graphql_name='pullRequestReviewContributionsByRepository', args=sgqlc.types.ArgDict((
        ('max_repositories', sgqlc.types.Arg(Int, graphql_name='maxRepositories', default=25)),
))
    )
    repository_contributions = sgqlc.types.Field(sgqlc.types.non_null('CreatedRepositoryContributionConnection'), graphql_name='repositoryContributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('order_by', sgqlc.types.Arg(ContributionOrder, graphql_name='orderBy', default={'field': 'OCCURRED_AT', 'direction': 'DESC'})),
))
    )
    restricted_contributions_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='restrictedContributionsCount')
    started_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='startedAt')
    total_commit_contributions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCommitContributions')
    total_issue_contributions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalIssueContributions', args=sgqlc.types.ArgDict((
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
))
    )
    total_pull_request_contributions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalPullRequestContributions', args=sgqlc.types.ArgDict((
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
))
    )
    total_pull_request_review_contributions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalPullRequestReviewContributions')
    total_repositories_with_contributed_commits = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRepositoriesWithContributedCommits')
    total_repositories_with_contributed_issues = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRepositoriesWithContributedIssues', args=sgqlc.types.ArgDict((
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
))
    )
    total_repositories_with_contributed_pull_request_reviews = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRepositoriesWithContributedPullRequestReviews')
    total_repositories_with_contributed_pull_requests = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRepositoriesWithContributedPullRequests', args=sgqlc.types.ArgDict((
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
        ('exclude_popular', sgqlc.types.Arg(Boolean, graphql_name='excludePopular', default=False)),
))
    )
    total_repository_contributions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalRepositoryContributions', args=sgqlc.types.ArgDict((
        ('exclude_first', sgqlc.types.Arg(Boolean, graphql_name='excludeFirst', default=False)),
))
    )
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')


class ConvertProjectCardNoteToIssuePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_card = sgqlc.types.Field('ProjectCard', graphql_name='projectCard')


class CreateBranchProtectionRulePayload(sgqlc.types.Type):
    __schema__ = github_schema
    branch_protection_rule = sgqlc.types.Field('BranchProtectionRule', graphql_name='branchProtectionRule')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateEnterpriseOrganizationPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')


class CreateIssuePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class CreateProjectPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field('Project', graphql_name='project')


class CreatePullRequestPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class CreateRefPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ref = sgqlc.types.Field('Ref', graphql_name='ref')


class CreateRepositoryPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class CreateTeamDiscussionCommentPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    team_discussion_comment = sgqlc.types.Field('TeamDiscussionComment', graphql_name='teamDiscussionComment')


class CreateTeamDiscussionPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    team_discussion = sgqlc.types.Field('TeamDiscussion', graphql_name='teamDiscussion')


class CreatedCommitContributionConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('CreatedCommitContributionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CreatedCommitContribution'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CreatedCommitContributionEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CreatedCommitContribution', graphql_name='node')


class CreatedIssueContributionConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('CreatedIssueContributionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CreatedIssueContribution'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CreatedIssueContributionEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CreatedIssueContribution', graphql_name='node')


class CreatedPullRequestContributionConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('CreatedPullRequestContributionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CreatedPullRequestContribution'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CreatedPullRequestContributionEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CreatedPullRequestContribution', graphql_name='node')


class CreatedPullRequestReviewContributionConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('CreatedPullRequestReviewContributionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CreatedPullRequestReviewContribution'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CreatedPullRequestReviewContributionEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CreatedPullRequestReviewContribution', graphql_name='node')


class CreatedRepositoryContributionConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('CreatedRepositoryContributionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('CreatedRepositoryContribution'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CreatedRepositoryContributionEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('CreatedRepositoryContribution', graphql_name='node')


class DeclineTopicSuggestionPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    topic = sgqlc.types.Field('Topic', graphql_name='topic')


class Deletable(sgqlc.types.Interface):
    __schema__ = github_schema
    viewer_can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelete')


class DeleteBranchProtectionRulePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteIssueCommentPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteIssuePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class DeleteProjectCardPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    column = sgqlc.types.Field('ProjectColumn', graphql_name='column')
    deleted_card_id = sgqlc.types.Field(ID, graphql_name='deletedCardId')


class DeleteProjectColumnPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_column_id = sgqlc.types.Field(ID, graphql_name='deletedColumnId')
    project = sgqlc.types.Field('Project', graphql_name='project')


class DeleteProjectPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    owner = sgqlc.types.Field('ProjectOwner', graphql_name='owner')


class DeletePullRequestReviewCommentPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field('PullRequestReview', graphql_name='pullRequestReview')


class DeletePullRequestReviewPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field('PullRequestReview', graphql_name='pullRequestReview')


class DeleteRefPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteTeamDiscussionCommentPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeleteTeamDiscussionPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class DeployKeyConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('DeployKeyEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('DeployKey'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeployKeyEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('DeployKey', graphql_name='node')


class DeploymentConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('DeploymentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Deployment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeploymentEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Deployment', graphql_name='node')


class DeploymentStatusConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('DeploymentStatusEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('DeploymentStatus'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class DeploymentStatusEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('DeploymentStatus', graphql_name='node')


class DismissPullRequestReviewPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field('PullRequestReview', graphql_name='pullRequestReview')


class EnterpriseAdministratorConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseAdministratorEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseAdministratorEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('User', graphql_name='node')
    role = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseAdministratorRole), graphql_name='role')


class EnterpriseAdministratorInvitationConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseAdministratorInvitationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseAdministratorInvitation'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseAdministratorInvitationEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseAdministratorInvitation', graphql_name='node')


class EnterpriseAuditEntryData(sgqlc.types.Interface):
    __schema__ = github_schema
    enterprise_resource_path = sgqlc.types.Field(URI, graphql_name='enterpriseResourcePath')
    enterprise_slug = sgqlc.types.Field(String, graphql_name='enterpriseSlug')
    enterprise_url = sgqlc.types.Field(URI, graphql_name='enterpriseUrl')


class EnterpriseBillingInfo(sgqlc.types.Type):
    __schema__ = github_schema
    all_licensable_users_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='allLicensableUsersCount')
    asset_packs = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='assetPacks')
    bandwidth_quota = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='bandwidthQuota')
    bandwidth_usage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='bandwidthUsage')
    bandwidth_usage_percentage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='bandwidthUsagePercentage')
    storage_quota = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='storageQuota')
    storage_usage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='storageUsage')
    storage_usage_percentage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='storageUsagePercentage')
    total_available_licenses = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalAvailableLicenses')
    total_licenses = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalLicenses')


class EnterpriseEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Enterprise', graphql_name='node')


class EnterpriseMemberConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseMemberEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseMember'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseMemberEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    is_unlicensed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUnlicensed')
    node = sgqlc.types.Field('EnterpriseMember', graphql_name='node')


class EnterpriseOrganizationMembershipConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseOrganizationMembershipEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Organization'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseOrganizationMembershipEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Organization', graphql_name='node')
    role = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseUserAccountMembershipRole), graphql_name='role')


class EnterpriseOutsideCollaboratorConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseOutsideCollaboratorEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseOutsideCollaboratorEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    is_unlicensed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUnlicensed')
    node = sgqlc.types.Field('User', graphql_name='node')
    repositories = sgqlc.types.Field(sgqlc.types.non_null('EnterpriseRepositoryInfoConnection'), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default={'field': 'NAME', 'direction': 'ASC'})),
))
    )


class EnterpriseOwnerInfo(sgqlc.types.Type):
    __schema__ = github_schema
    action_execution_capability_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='actionExecutionCapabilitySettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    admins = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseAdministratorConnection), graphql_name='admins', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('role', sgqlc.types.Arg(EnterpriseAdministratorRole, graphql_name='role', default=None)),
        ('order_by', sgqlc.types.Arg(EnterpriseMemberOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    affiliated_users_with_two_factor_disabled = sgqlc.types.Field(sgqlc.types.non_null('UserConnection'), graphql_name='affiliatedUsersWithTwoFactorDisabled', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    affiliated_users_with_two_factor_disabled_exist = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='affiliatedUsersWithTwoFactorDisabledExist')
    allow_private_repository_forking_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='allowPrivateRepositoryForkingSetting')
    allow_private_repository_forking_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='allowPrivateRepositoryForkingSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    default_repository_permission_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseDefaultRepositoryPermissionSettingValue), graphql_name='defaultRepositoryPermissionSetting')
    default_repository_permission_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='defaultRepositoryPermissionSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(DefaultRepositoryPermissionField), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    enterprise_server_installations = sgqlc.types.Field(sgqlc.types.non_null('EnterpriseServerInstallationConnection'), graphql_name='enterpriseServerInstallations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('connected_only', sgqlc.types.Arg(Boolean, graphql_name='connectedOnly', default=False)),
        ('order_by', sgqlc.types.Arg(EnterpriseServerInstallationOrder, graphql_name='orderBy', default={'field': 'HOST_NAME', 'direction': 'ASC'})),
))
    )
    is_updating_default_repository_permission = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUpdatingDefaultRepositoryPermission')
    is_updating_two_factor_requirement = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUpdatingTwoFactorRequirement')
    members_can_change_repository_visibility_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='membersCanChangeRepositoryVisibilitySetting')
    members_can_change_repository_visibility_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='membersCanChangeRepositoryVisibilitySettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    members_can_create_internal_repositories_setting = sgqlc.types.Field(Boolean, graphql_name='membersCanCreateInternalRepositoriesSetting')
    members_can_create_private_repositories_setting = sgqlc.types.Field(Boolean, graphql_name='membersCanCreatePrivateRepositoriesSetting')
    members_can_create_public_repositories_setting = sgqlc.types.Field(Boolean, graphql_name='membersCanCreatePublicRepositoriesSetting')
    members_can_create_repositories_setting = sgqlc.types.Field(EnterpriseMembersCanCreateRepositoriesSettingValue, graphql_name='membersCanCreateRepositoriesSetting')
    members_can_create_repositories_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='membersCanCreateRepositoriesSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(OrganizationMembersCanCreateRepositoriesSettingValue), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    members_can_delete_issues_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='membersCanDeleteIssuesSetting')
    members_can_delete_issues_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='membersCanDeleteIssuesSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    members_can_delete_repositories_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='membersCanDeleteRepositoriesSetting')
    members_can_delete_repositories_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='membersCanDeleteRepositoriesSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    members_can_invite_collaborators_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='membersCanInviteCollaboratorsSetting')
    members_can_invite_collaborators_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='membersCanInviteCollaboratorsSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    members_can_make_purchases_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseMembersCanMakePurchasesSettingValue), graphql_name='membersCanMakePurchasesSetting')
    members_can_update_protected_branches_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='membersCanUpdateProtectedBranchesSetting')
    members_can_update_protected_branches_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='membersCanUpdateProtectedBranchesSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    members_can_view_dependency_insights_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='membersCanViewDependencyInsightsSetting')
    members_can_view_dependency_insights_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='membersCanViewDependencyInsightsSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    organization_projects_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='organizationProjectsSetting')
    organization_projects_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='organizationProjectsSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    outside_collaborators = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseOutsideCollaboratorConnection), graphql_name='outsideCollaborators', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(String, graphql_name='login', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(EnterpriseMemberOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
        ('visibility', sgqlc.types.Arg(RepositoryVisibility, graphql_name='visibility', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pending_admin_invitations = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseAdministratorInvitationConnection), graphql_name='pendingAdminInvitations', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(EnterpriseAdministratorInvitationOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'DESC'})),
        ('role', sgqlc.types.Arg(EnterpriseAdministratorRole, graphql_name='role', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pending_collaborators = sgqlc.types.Field(sgqlc.types.non_null('EnterprisePendingCollaboratorConnection'), graphql_name='pendingCollaborators', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryInvitationOrder, graphql_name='orderBy', default={'field': 'INVITEE_LOGIN', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pending_member_invitations = sgqlc.types.Field(sgqlc.types.non_null('EnterprisePendingMemberInvitationConnection'), graphql_name='pendingMemberInvitations', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    repository_projects_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='repositoryProjectsSetting')
    repository_projects_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='repositoryProjectsSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    saml_identity_provider = sgqlc.types.Field('EnterpriseIdentityProvider', graphql_name='samlIdentityProvider')
    saml_identity_provider_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='samlIdentityProviderSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(IdentityProviderConfigurationState), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    team_discussions_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledDisabledSettingValue), graphql_name='teamDiscussionsSetting')
    team_discussions_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='teamDiscussionsSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )
    two_factor_required_setting = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseEnabledSettingValue), graphql_name='twoFactorRequiredSetting')
    two_factor_required_setting_organizations = sgqlc.types.Field(sgqlc.types.non_null('OrganizationConnection'), graphql_name='twoFactorRequiredSettingOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('value', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='value', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
))
    )


class EnterprisePendingCollaboratorConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterprisePendingCollaboratorEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterprisePendingCollaboratorEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    is_unlicensed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUnlicensed')
    node = sgqlc.types.Field('User', graphql_name='node')
    repositories = sgqlc.types.Field(sgqlc.types.non_null('EnterpriseRepositoryInfoConnection'), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default={'field': 'NAME', 'direction': 'ASC'})),
))
    )


class EnterprisePendingMemberInvitationConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterprisePendingMemberInvitationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('OrganizationInvitation'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    total_unique_user_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalUniqueUserCount')


class EnterprisePendingMemberInvitationEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    is_unlicensed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUnlicensed')
    node = sgqlc.types.Field('OrganizationInvitation', graphql_name='node')


class EnterpriseRepositoryInfoConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseRepositoryInfoEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseRepositoryInfo'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseRepositoryInfoEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseRepositoryInfo', graphql_name='node')


class EnterpriseServerInstallationConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerInstallationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerInstallation'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseServerInstallationEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseServerInstallation', graphql_name='node')


class EnterpriseServerUserAccountConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerUserAccountEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerUserAccount'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseServerUserAccountEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseServerUserAccount', graphql_name='node')


class EnterpriseServerUserAccountEmailConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerUserAccountEmailEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerUserAccountEmail'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseServerUserAccountEmailEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseServerUserAccountEmail', graphql_name='node')


class EnterpriseServerUserAccountsUploadConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerUserAccountsUploadEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseServerUserAccountsUpload'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseServerUserAccountsUploadEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseServerUserAccountsUpload', graphql_name='node')


class EnterpriseUserAccountConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseUserAccountEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('EnterpriseUserAccount'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnterpriseUserAccountEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('EnterpriseUserAccount', graphql_name='node')


class ExternalIdentityConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ExternalIdentityEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ExternalIdentity'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ExternalIdentityEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ExternalIdentity', graphql_name='node')


class ExternalIdentitySamlAttributes(sgqlc.types.Type):
    __schema__ = github_schema
    name_id = sgqlc.types.Field(String, graphql_name='nameId')


class ExternalIdentityScimAttributes(sgqlc.types.Type):
    __schema__ = github_schema
    username = sgqlc.types.Field(String, graphql_name='username')


class FollowUserPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user = sgqlc.types.Field('User', graphql_name='user')


class FollowerConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FollowingConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class FundingLink(sgqlc.types.Type):
    __schema__ = github_schema
    platform = sgqlc.types.Field(sgqlc.types.non_null(FundingPlatform), graphql_name='platform')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class GistCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('GistCommentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('GistComment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class GistCommentEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('GistComment', graphql_name='node')


class GistConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('GistEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Gist'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class GistEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Gist', graphql_name='node')


class GistFile(sgqlc.types.Type):
    __schema__ = github_schema
    encoded_name = sgqlc.types.Field(String, graphql_name='encodedName')
    encoding = sgqlc.types.Field(String, graphql_name='encoding')
    extension = sgqlc.types.Field(String, graphql_name='extension')
    is_image = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isImage')
    is_truncated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTruncated')
    language = sgqlc.types.Field('Language', graphql_name='language')
    name = sgqlc.types.Field(String, graphql_name='name')
    size = sgqlc.types.Field(Int, graphql_name='size')
    text = sgqlc.types.Field(String, graphql_name='text', args=sgqlc.types.ArgDict((
        ('truncate', sgqlc.types.Arg(Int, graphql_name='truncate', default=None)),
))
    )


class GitActor(sgqlc.types.Type):
    __schema__ = github_schema
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    date = sgqlc.types.Field(GitTimestamp, graphql_name='date')
    email = sgqlc.types.Field(String, graphql_name='email')
    name = sgqlc.types.Field(String, graphql_name='name')
    user = sgqlc.types.Field('User', graphql_name='user')


class GitHubMetadata(sgqlc.types.Type):
    __schema__ = github_schema
    git_hub_services_sha = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='gitHubServicesSha')
    git_ip_addresses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='gitIpAddresses')
    hook_ip_addresses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='hookIpAddresses')
    importer_ip_addresses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='importerIpAddresses')
    is_password_authentication_verifiable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPasswordAuthenticationVerifiable')
    pages_ip_addresses = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='pagesIpAddresses')


class GitObject(sgqlc.types.Interface):
    __schema__ = github_schema
    abbreviated_oid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='abbreviatedOid')
    commit_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitResourcePath')
    commit_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class GitSignature(sgqlc.types.Interface):
    __schema__ = github_schema
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    is_valid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isValid')
    payload = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='payload')
    signature = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='signature')
    signer = sgqlc.types.Field('User', graphql_name='signer')
    state = sgqlc.types.Field(sgqlc.types.non_null(GitSignatureState), graphql_name='state')
    was_signed_by_git_hub = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='wasSignedByGitHub')


class Hovercard(sgqlc.types.Type):
    __schema__ = github_schema
    contexts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('HovercardContext'))), graphql_name='contexts')


class HovercardContext(sgqlc.types.Interface):
    __schema__ = github_schema
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    octicon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='octicon')


class InviteEnterpriseAdminPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invitation = sgqlc.types.Field('EnterpriseAdministratorInvitation', graphql_name='invitation')


class IssueCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('IssueCommentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('IssueComment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueCommentEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('IssueComment', graphql_name='node')


class IssueConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('IssueEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Issue'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueContributionsByRepository(sgqlc.types.Type):
    __schema__ = github_schema
    contributions = sgqlc.types.Field(sgqlc.types.non_null(CreatedIssueContributionConnection), graphql_name='contributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ContributionOrder, graphql_name='orderBy', default={'field': 'OCCURRED_AT', 'direction': 'DESC'})),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class IssueEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Issue', graphql_name='node')


class IssueOrPullRequestEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('IssueOrPullRequest', graphql_name='node')


class IssueTimelineConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('IssueTimelineItemEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('IssueTimelineItem'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class IssueTimelineItemEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('IssueTimelineItem', graphql_name='node')


class IssueTimelineItemsConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('IssueTimelineItemsEdge'), graphql_name='edges')
    filtered_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='filteredCount')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('IssueTimelineItems'), graphql_name='nodes')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class IssueTimelineItemsEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('IssueTimelineItems', graphql_name='node')


class LabelConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('LabelEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Label'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class LabelEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Label', graphql_name='node')


class Labelable(sgqlc.types.Interface):
    __schema__ = github_schema
    labels = sgqlc.types.Field(LabelConnection, graphql_name='labels', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class LanguageConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('LanguageEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Language'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    total_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalSize')


class LanguageEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Language'), graphql_name='node')
    size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='size')


class LicenseRule(sgqlc.types.Type):
    __schema__ = github_schema
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='label')


class LinkRepositoryToProjectPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field('Project', graphql_name='project')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class LockLockablePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    locked_record = sgqlc.types.Field('Lockable', graphql_name='lockedRecord')


class Lockable(sgqlc.types.Interface):
    __schema__ = github_schema
    active_lock_reason = sgqlc.types.Field(LockReason, graphql_name='activeLockReason')
    locked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='locked')


class MarketplaceListingConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('MarketplaceListingEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('MarketplaceListing'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MarketplaceListingEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('MarketplaceListing', graphql_name='node')


class MemberStatusable(sgqlc.types.Interface):
    __schema__ = github_schema
    member_statuses = sgqlc.types.Field(sgqlc.types.non_null('UserStatusConnection'), graphql_name='memberStatuses', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(UserStatusOrder, graphql_name='orderBy', default={'field': 'UPDATED_AT', 'direction': 'DESC'})),
))
    )


class MergeBranchPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    merge_commit = sgqlc.types.Field('Commit', graphql_name='mergeCommit')


class MergePullRequestPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class MilestoneConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('MilestoneEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Milestone'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class MilestoneEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Milestone', graphql_name='node')


class MoveProjectCardPayload(sgqlc.types.Type):
    __schema__ = github_schema
    card_edge = sgqlc.types.Field('ProjectCardEdge', graphql_name='cardEdge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class MoveProjectColumnPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    column_edge = sgqlc.types.Field('ProjectColumnEdge', graphql_name='columnEdge')


class Mutation(sgqlc.types.Type):
    __schema__ = github_schema
    accept_enterprise_administrator_invitation = sgqlc.types.Field(AcceptEnterpriseAdministratorInvitationPayload, graphql_name='acceptEnterpriseAdministratorInvitation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AcceptEnterpriseAdministratorInvitationInput), graphql_name='input', default=None)),
))
    )
    accept_topic_suggestion = sgqlc.types.Field(AcceptTopicSuggestionPayload, graphql_name='acceptTopicSuggestion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AcceptTopicSuggestionInput), graphql_name='input', default=None)),
))
    )
    add_assignees_to_assignable = sgqlc.types.Field(AddAssigneesToAssignablePayload, graphql_name='addAssigneesToAssignable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddAssigneesToAssignableInput), graphql_name='input', default=None)),
))
    )
    add_comment = sgqlc.types.Field(AddCommentPayload, graphql_name='addComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddCommentInput), graphql_name='input', default=None)),
))
    )
    add_labels_to_labelable = sgqlc.types.Field(AddLabelsToLabelablePayload, graphql_name='addLabelsToLabelable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddLabelsToLabelableInput), graphql_name='input', default=None)),
))
    )
    add_project_card = sgqlc.types.Field(AddProjectCardPayload, graphql_name='addProjectCard', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddProjectCardInput), graphql_name='input', default=None)),
))
    )
    add_project_column = sgqlc.types.Field(AddProjectColumnPayload, graphql_name='addProjectColumn', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddProjectColumnInput), graphql_name='input', default=None)),
))
    )
    add_pull_request_review = sgqlc.types.Field(AddPullRequestReviewPayload, graphql_name='addPullRequestReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddPullRequestReviewInput), graphql_name='input', default=None)),
))
    )
    add_pull_request_review_comment = sgqlc.types.Field(AddPullRequestReviewCommentPayload, graphql_name='addPullRequestReviewComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddPullRequestReviewCommentInput), graphql_name='input', default=None)),
))
    )
    add_reaction = sgqlc.types.Field(AddReactionPayload, graphql_name='addReaction', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddReactionInput), graphql_name='input', default=None)),
))
    )
    add_star = sgqlc.types.Field(AddStarPayload, graphql_name='addStar', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddStarInput), graphql_name='input', default=None)),
))
    )
    archive_repository = sgqlc.types.Field(ArchiveRepositoryPayload, graphql_name='archiveRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ArchiveRepositoryInput), graphql_name='input', default=None)),
))
    )
    cancel_enterprise_admin_invitation = sgqlc.types.Field(CancelEnterpriseAdminInvitationPayload, graphql_name='cancelEnterpriseAdminInvitation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CancelEnterpriseAdminInvitationInput), graphql_name='input', default=None)),
))
    )
    change_user_status = sgqlc.types.Field(ChangeUserStatusPayload, graphql_name='changeUserStatus', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ChangeUserStatusInput), graphql_name='input', default=None)),
))
    )
    clear_labels_from_labelable = sgqlc.types.Field(ClearLabelsFromLabelablePayload, graphql_name='clearLabelsFromLabelable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ClearLabelsFromLabelableInput), graphql_name='input', default=None)),
))
    )
    clone_project = sgqlc.types.Field(CloneProjectPayload, graphql_name='cloneProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CloneProjectInput), graphql_name='input', default=None)),
))
    )
    clone_template_repository = sgqlc.types.Field(CloneTemplateRepositoryPayload, graphql_name='cloneTemplateRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CloneTemplateRepositoryInput), graphql_name='input', default=None)),
))
    )
    close_issue = sgqlc.types.Field(CloseIssuePayload, graphql_name='closeIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CloseIssueInput), graphql_name='input', default=None)),
))
    )
    close_pull_request = sgqlc.types.Field(ClosePullRequestPayload, graphql_name='closePullRequest', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ClosePullRequestInput), graphql_name='input', default=None)),
))
    )
    convert_project_card_note_to_issue = sgqlc.types.Field(ConvertProjectCardNoteToIssuePayload, graphql_name='convertProjectCardNoteToIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ConvertProjectCardNoteToIssueInput), graphql_name='input', default=None)),
))
    )
    create_branch_protection_rule = sgqlc.types.Field(CreateBranchProtectionRulePayload, graphql_name='createBranchProtectionRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateBranchProtectionRuleInput), graphql_name='input', default=None)),
))
    )
    create_enterprise_organization = sgqlc.types.Field(CreateEnterpriseOrganizationPayload, graphql_name='createEnterpriseOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEnterpriseOrganizationInput), graphql_name='input', default=None)),
))
    )
    create_issue = sgqlc.types.Field(CreateIssuePayload, graphql_name='createIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateIssueInput), graphql_name='input', default=None)),
))
    )
    create_project = sgqlc.types.Field(CreateProjectPayload, graphql_name='createProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateProjectInput), graphql_name='input', default=None)),
))
    )
    create_pull_request = sgqlc.types.Field(CreatePullRequestPayload, graphql_name='createPullRequest', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreatePullRequestInput), graphql_name='input', default=None)),
))
    )
    create_ref = sgqlc.types.Field(CreateRefPayload, graphql_name='createRef', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateRefInput), graphql_name='input', default=None)),
))
    )
    create_repository = sgqlc.types.Field(CreateRepositoryPayload, graphql_name='createRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateRepositoryInput), graphql_name='input', default=None)),
))
    )
    create_team_discussion = sgqlc.types.Field(CreateTeamDiscussionPayload, graphql_name='createTeamDiscussion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTeamDiscussionInput), graphql_name='input', default=None)),
))
    )
    create_team_discussion_comment = sgqlc.types.Field(CreateTeamDiscussionCommentPayload, graphql_name='createTeamDiscussionComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTeamDiscussionCommentInput), graphql_name='input', default=None)),
))
    )
    decline_topic_suggestion = sgqlc.types.Field(DeclineTopicSuggestionPayload, graphql_name='declineTopicSuggestion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeclineTopicSuggestionInput), graphql_name='input', default=None)),
))
    )
    delete_branch_protection_rule = sgqlc.types.Field(DeleteBranchProtectionRulePayload, graphql_name='deleteBranchProtectionRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteBranchProtectionRuleInput), graphql_name='input', default=None)),
))
    )
    delete_issue = sgqlc.types.Field(DeleteIssuePayload, graphql_name='deleteIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteIssueInput), graphql_name='input', default=None)),
))
    )
    delete_issue_comment = sgqlc.types.Field(DeleteIssueCommentPayload, graphql_name='deleteIssueComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteIssueCommentInput), graphql_name='input', default=None)),
))
    )
    delete_project = sgqlc.types.Field(DeleteProjectPayload, graphql_name='deleteProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectInput), graphql_name='input', default=None)),
))
    )
    delete_project_card = sgqlc.types.Field(DeleteProjectCardPayload, graphql_name='deleteProjectCard', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectCardInput), graphql_name='input', default=None)),
))
    )
    delete_project_column = sgqlc.types.Field(DeleteProjectColumnPayload, graphql_name='deleteProjectColumn', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProjectColumnInput), graphql_name='input', default=None)),
))
    )
    delete_pull_request_review = sgqlc.types.Field(DeletePullRequestReviewPayload, graphql_name='deletePullRequestReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeletePullRequestReviewInput), graphql_name='input', default=None)),
))
    )
    delete_pull_request_review_comment = sgqlc.types.Field(DeletePullRequestReviewCommentPayload, graphql_name='deletePullRequestReviewComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeletePullRequestReviewCommentInput), graphql_name='input', default=None)),
))
    )
    delete_ref = sgqlc.types.Field(DeleteRefPayload, graphql_name='deleteRef', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteRefInput), graphql_name='input', default=None)),
))
    )
    delete_team_discussion = sgqlc.types.Field(DeleteTeamDiscussionPayload, graphql_name='deleteTeamDiscussion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteTeamDiscussionInput), graphql_name='input', default=None)),
))
    )
    delete_team_discussion_comment = sgqlc.types.Field(DeleteTeamDiscussionCommentPayload, graphql_name='deleteTeamDiscussionComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteTeamDiscussionCommentInput), graphql_name='input', default=None)),
))
    )
    dismiss_pull_request_review = sgqlc.types.Field(DismissPullRequestReviewPayload, graphql_name='dismissPullRequestReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DismissPullRequestReviewInput), graphql_name='input', default=None)),
))
    )
    follow_user = sgqlc.types.Field(FollowUserPayload, graphql_name='followUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(FollowUserInput), graphql_name='input', default=None)),
))
    )
    invite_enterprise_admin = sgqlc.types.Field(InviteEnterpriseAdminPayload, graphql_name='inviteEnterpriseAdmin', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(InviteEnterpriseAdminInput), graphql_name='input', default=None)),
))
    )
    link_repository_to_project = sgqlc.types.Field(LinkRepositoryToProjectPayload, graphql_name='linkRepositoryToProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LinkRepositoryToProjectInput), graphql_name='input', default=None)),
))
    )
    lock_lockable = sgqlc.types.Field(LockLockablePayload, graphql_name='lockLockable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LockLockableInput), graphql_name='input', default=None)),
))
    )
    merge_branch = sgqlc.types.Field(MergeBranchPayload, graphql_name='mergeBranch', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MergeBranchInput), graphql_name='input', default=None)),
))
    )
    merge_pull_request = sgqlc.types.Field(MergePullRequestPayload, graphql_name='mergePullRequest', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MergePullRequestInput), graphql_name='input', default=None)),
))
    )
    move_project_card = sgqlc.types.Field(MoveProjectCardPayload, graphql_name='moveProjectCard', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MoveProjectCardInput), graphql_name='input', default=None)),
))
    )
    move_project_column = sgqlc.types.Field(MoveProjectColumnPayload, graphql_name='moveProjectColumn', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(MoveProjectColumnInput), graphql_name='input', default=None)),
))
    )
    regenerate_enterprise_identity_provider_recovery_codes = sgqlc.types.Field('RegenerateEnterpriseIdentityProviderRecoveryCodesPayload', graphql_name='regenerateEnterpriseIdentityProviderRecoveryCodes', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RegenerateEnterpriseIdentityProviderRecoveryCodesInput), graphql_name='input', default=None)),
))
    )
    remove_assignees_from_assignable = sgqlc.types.Field('RemoveAssigneesFromAssignablePayload', graphql_name='removeAssigneesFromAssignable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveAssigneesFromAssignableInput), graphql_name='input', default=None)),
))
    )
    remove_enterprise_admin = sgqlc.types.Field('RemoveEnterpriseAdminPayload', graphql_name='removeEnterpriseAdmin', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveEnterpriseAdminInput), graphql_name='input', default=None)),
))
    )
    remove_enterprise_organization = sgqlc.types.Field('RemoveEnterpriseOrganizationPayload', graphql_name='removeEnterpriseOrganization', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveEnterpriseOrganizationInput), graphql_name='input', default=None)),
))
    )
    remove_labels_from_labelable = sgqlc.types.Field('RemoveLabelsFromLabelablePayload', graphql_name='removeLabelsFromLabelable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveLabelsFromLabelableInput), graphql_name='input', default=None)),
))
    )
    remove_outside_collaborator = sgqlc.types.Field('RemoveOutsideCollaboratorPayload', graphql_name='removeOutsideCollaborator', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveOutsideCollaboratorInput), graphql_name='input', default=None)),
))
    )
    remove_reaction = sgqlc.types.Field('RemoveReactionPayload', graphql_name='removeReaction', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveReactionInput), graphql_name='input', default=None)),
))
    )
    remove_star = sgqlc.types.Field('RemoveStarPayload', graphql_name='removeStar', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RemoveStarInput), graphql_name='input', default=None)),
))
    )
    reopen_issue = sgqlc.types.Field('ReopenIssuePayload', graphql_name='reopenIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReopenIssueInput), graphql_name='input', default=None)),
))
    )
    reopen_pull_request = sgqlc.types.Field('ReopenPullRequestPayload', graphql_name='reopenPullRequest', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ReopenPullRequestInput), graphql_name='input', default=None)),
))
    )
    request_reviews = sgqlc.types.Field('RequestReviewsPayload', graphql_name='requestReviews', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RequestReviewsInput), graphql_name='input', default=None)),
))
    )
    resolve_review_thread = sgqlc.types.Field('ResolveReviewThreadPayload', graphql_name='resolveReviewThread', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ResolveReviewThreadInput), graphql_name='input', default=None)),
))
    )
    submit_pull_request_review = sgqlc.types.Field('SubmitPullRequestReviewPayload', graphql_name='submitPullRequestReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SubmitPullRequestReviewInput), graphql_name='input', default=None)),
))
    )
    transfer_issue = sgqlc.types.Field('TransferIssuePayload', graphql_name='transferIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(TransferIssueInput), graphql_name='input', default=None)),
))
    )
    unarchive_repository = sgqlc.types.Field('UnarchiveRepositoryPayload', graphql_name='unarchiveRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnarchiveRepositoryInput), graphql_name='input', default=None)),
))
    )
    unfollow_user = sgqlc.types.Field('UnfollowUserPayload', graphql_name='unfollowUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnfollowUserInput), graphql_name='input', default=None)),
))
    )
    unlink_repository_from_project = sgqlc.types.Field('UnlinkRepositoryFromProjectPayload', graphql_name='unlinkRepositoryFromProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnlinkRepositoryFromProjectInput), graphql_name='input', default=None)),
))
    )
    unlock_lockable = sgqlc.types.Field('UnlockLockablePayload', graphql_name='unlockLockable', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnlockLockableInput), graphql_name='input', default=None)),
))
    )
    unmark_issue_as_duplicate = sgqlc.types.Field('UnmarkIssueAsDuplicatePayload', graphql_name='unmarkIssueAsDuplicate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnmarkIssueAsDuplicateInput), graphql_name='input', default=None)),
))
    )
    unresolve_review_thread = sgqlc.types.Field('UnresolveReviewThreadPayload', graphql_name='unresolveReviewThread', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UnresolveReviewThreadInput), graphql_name='input', default=None)),
))
    )
    update_branch_protection_rule = sgqlc.types.Field('UpdateBranchProtectionRulePayload', graphql_name='updateBranchProtectionRule', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateBranchProtectionRuleInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_action_execution_capability_setting = sgqlc.types.Field('UpdateEnterpriseActionExecutionCapabilitySettingPayload', graphql_name='updateEnterpriseActionExecutionCapabilitySetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseActionExecutionCapabilitySettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_administrator_role = sgqlc.types.Field('UpdateEnterpriseAdministratorRolePayload', graphql_name='updateEnterpriseAdministratorRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseAdministratorRoleInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_allow_private_repository_forking_setting = sgqlc.types.Field('UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayload', graphql_name='updateEnterpriseAllowPrivateRepositoryForkingSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseAllowPrivateRepositoryForkingSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_default_repository_permission_setting = sgqlc.types.Field('UpdateEnterpriseDefaultRepositoryPermissionSettingPayload', graphql_name='updateEnterpriseDefaultRepositoryPermissionSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseDefaultRepositoryPermissionSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_change_repository_visibility_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayload', graphql_name='updateEnterpriseMembersCanChangeRepositoryVisibilitySetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_create_repositories_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanCreateRepositoriesSettingPayload', graphql_name='updateEnterpriseMembersCanCreateRepositoriesSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanCreateRepositoriesSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_delete_issues_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanDeleteIssuesSettingPayload', graphql_name='updateEnterpriseMembersCanDeleteIssuesSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanDeleteIssuesSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_delete_repositories_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayload', graphql_name='updateEnterpriseMembersCanDeleteRepositoriesSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanDeleteRepositoriesSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_invite_collaborators_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayload', graphql_name='updateEnterpriseMembersCanInviteCollaboratorsSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanInviteCollaboratorsSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_make_purchases_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanMakePurchasesSettingPayload', graphql_name='updateEnterpriseMembersCanMakePurchasesSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanMakePurchasesSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_update_protected_branches_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayload', graphql_name='updateEnterpriseMembersCanUpdateProtectedBranchesSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_members_can_view_dependency_insights_setting = sgqlc.types.Field('UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayload', graphql_name='updateEnterpriseMembersCanViewDependencyInsightsSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseMembersCanViewDependencyInsightsSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_organization_projects_setting = sgqlc.types.Field('UpdateEnterpriseOrganizationProjectsSettingPayload', graphql_name='updateEnterpriseOrganizationProjectsSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseOrganizationProjectsSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_profile = sgqlc.types.Field('UpdateEnterpriseProfilePayload', graphql_name='updateEnterpriseProfile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseProfileInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_repository_projects_setting = sgqlc.types.Field('UpdateEnterpriseRepositoryProjectsSettingPayload', graphql_name='updateEnterpriseRepositoryProjectsSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseRepositoryProjectsSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_team_discussions_setting = sgqlc.types.Field('UpdateEnterpriseTeamDiscussionsSettingPayload', graphql_name='updateEnterpriseTeamDiscussionsSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseTeamDiscussionsSettingInput), graphql_name='input', default=None)),
))
    )
    update_enterprise_two_factor_authentication_required_setting = sgqlc.types.Field('UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayload', graphql_name='updateEnterpriseTwoFactorAuthenticationRequiredSetting', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateEnterpriseTwoFactorAuthenticationRequiredSettingInput), graphql_name='input', default=None)),
))
    )
    update_issue = sgqlc.types.Field('UpdateIssuePayload', graphql_name='updateIssue', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateIssueInput), graphql_name='input', default=None)),
))
    )
    update_issue_comment = sgqlc.types.Field('UpdateIssueCommentPayload', graphql_name='updateIssueComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateIssueCommentInput), graphql_name='input', default=None)),
))
    )
    update_project = sgqlc.types.Field('UpdateProjectPayload', graphql_name='updateProject', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectInput), graphql_name='input', default=None)),
))
    )
    update_project_card = sgqlc.types.Field('UpdateProjectCardPayload', graphql_name='updateProjectCard', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectCardInput), graphql_name='input', default=None)),
))
    )
    update_project_column = sgqlc.types.Field('UpdateProjectColumnPayload', graphql_name='updateProjectColumn', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProjectColumnInput), graphql_name='input', default=None)),
))
    )
    update_pull_request = sgqlc.types.Field('UpdatePullRequestPayload', graphql_name='updatePullRequest', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePullRequestInput), graphql_name='input', default=None)),
))
    )
    update_pull_request_review = sgqlc.types.Field('UpdatePullRequestReviewPayload', graphql_name='updatePullRequestReview', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePullRequestReviewInput), graphql_name='input', default=None)),
))
    )
    update_pull_request_review_comment = sgqlc.types.Field('UpdatePullRequestReviewCommentPayload', graphql_name='updatePullRequestReviewComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdatePullRequestReviewCommentInput), graphql_name='input', default=None)),
))
    )
    update_ref = sgqlc.types.Field('UpdateRefPayload', graphql_name='updateRef', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRefInput), graphql_name='input', default=None)),
))
    )
    update_repository = sgqlc.types.Field('UpdateRepositoryPayload', graphql_name='updateRepository', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateRepositoryInput), graphql_name='input', default=None)),
))
    )
    update_subscription = sgqlc.types.Field('UpdateSubscriptionPayload', graphql_name='updateSubscription', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSubscriptionInput), graphql_name='input', default=None)),
))
    )
    update_team_discussion = sgqlc.types.Field('UpdateTeamDiscussionPayload', graphql_name='updateTeamDiscussion', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTeamDiscussionInput), graphql_name='input', default=None)),
))
    )
    update_team_discussion_comment = sgqlc.types.Field('UpdateTeamDiscussionCommentPayload', graphql_name='updateTeamDiscussionComment', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTeamDiscussionCommentInput), graphql_name='input', default=None)),
))
    )
    update_topics = sgqlc.types.Field('UpdateTopicsPayload', graphql_name='updateTopics', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTopicsInput), graphql_name='input', default=None)),
))
    )


class Node(sgqlc.types.Interface):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class OauthApplicationAuditEntryData(sgqlc.types.Interface):
    __schema__ = github_schema
    oauth_application_name = sgqlc.types.Field(String, graphql_name='oauthApplicationName')
    oauth_application_resource_path = sgqlc.types.Field(URI, graphql_name='oauthApplicationResourcePath')
    oauth_application_url = sgqlc.types.Field(URI, graphql_name='oauthApplicationUrl')


class OrganizationAuditEntryConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('OrganizationAuditEntryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('OrganizationAuditEntry'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OrganizationAuditEntryData(sgqlc.types.Interface):
    __schema__ = github_schema
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')


class OrganizationAuditEntryEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('OrganizationAuditEntry', graphql_name='node')


class OrganizationConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('OrganizationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Organization'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OrganizationEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Organization', graphql_name='node')


class OrganizationInvitationConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('OrganizationInvitationEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('OrganizationInvitation'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OrganizationInvitationEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('OrganizationInvitation', graphql_name='node')


class OrganizationMemberConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('OrganizationMemberEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class OrganizationMemberEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    has_two_factor_enabled = sgqlc.types.Field(Boolean, graphql_name='hasTwoFactorEnabled')
    node = sgqlc.types.Field('User', graphql_name='node')
    role = sgqlc.types.Field(OrganizationMemberRole, graphql_name='role')


class PageInfo(sgqlc.types.Type):
    __schema__ = github_schema
    end_cursor = sgqlc.types.Field(String, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(String, graphql_name='startCursor')


class PermissionSource(sgqlc.types.Type):
    __schema__ = github_schema
    organization = sgqlc.types.Field(sgqlc.types.non_null('Organization'), graphql_name='organization')
    permission = sgqlc.types.Field(sgqlc.types.non_null(DefaultRepositoryPermissionField), graphql_name='permission')
    source = sgqlc.types.Field(sgqlc.types.non_null('PermissionGranter'), graphql_name='source')


class PinnableItemConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PinnableItemEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PinnableItem'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PinnableItemEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PinnableItem', graphql_name='node')


class ProfileItemShowcase(sgqlc.types.Type):
    __schema__ = github_schema
    has_pinned_items = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPinnedItems')
    items = sgqlc.types.Field(sgqlc.types.non_null(PinnableItemConnection), graphql_name='items', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class ProfileOwner(sgqlc.types.Interface):
    __schema__ = github_schema
    any_pinnable_items = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='anyPinnableItems', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(PinnableItemType, graphql_name='type', default=None)),
))
    )
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    item_showcase = sgqlc.types.Field(sgqlc.types.non_null(ProfileItemShowcase), graphql_name='itemShowcase')
    location = sgqlc.types.Field(String, graphql_name='location')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    name = sgqlc.types.Field(String, graphql_name='name')
    pinnable_items = sgqlc.types.Field(sgqlc.types.non_null(PinnableItemConnection), graphql_name='pinnableItems', args=sgqlc.types.ArgDict((
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PinnableItemType)), graphql_name='types', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pinned_items = sgqlc.types.Field(sgqlc.types.non_null(PinnableItemConnection), graphql_name='pinnedItems', args=sgqlc.types.ArgDict((
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PinnableItemType)), graphql_name='types', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pinned_items_remaining = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pinnedItemsRemaining')
    viewer_can_change_pinned_items = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanChangePinnedItems')
    website_url = sgqlc.types.Field(URI, graphql_name='websiteUrl')


class ProjectCardConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectCardEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProjectCard'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectCardEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProjectCard', graphql_name='node')


class ProjectColumnConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectColumnEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ProjectColumn'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectColumnEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ProjectColumn', graphql_name='node')


class ProjectConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ProjectEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Project'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProjectEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Project', graphql_name='node')


class ProjectOwner(sgqlc.types.Interface):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    project = sgqlc.types.Field('Project', graphql_name='project', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    projects = sgqlc.types.Field(sgqlc.types.non_null(ProjectConnection), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(ProjectOrder, graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectState)), graphql_name='states', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    projects_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsResourcePath')
    projects_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsUrl')
    viewer_can_create_projects = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanCreateProjects')


class PublicKeyConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PublicKeyEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PublicKey'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PublicKeyEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PublicKey', graphql_name='node')


class PullRequestChangedFile(sgqlc.types.Type):
    __schema__ = github_schema
    additions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='additions')
    deletions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='deletions')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')


class PullRequestChangedFileConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestChangedFileEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(PullRequestChangedFile), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestChangedFileEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(PullRequestChangedFile, graphql_name='node')


class PullRequestCommitConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestCommitEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestCommit'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestCommitEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestCommit', graphql_name='node')


class PullRequestConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequest'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestContributionsByRepository(sgqlc.types.Type):
    __schema__ = github_schema
    contributions = sgqlc.types.Field(sgqlc.types.non_null(CreatedPullRequestContributionConnection), graphql_name='contributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ContributionOrder, graphql_name='orderBy', default={'field': 'OCCURRED_AT', 'direction': 'DESC'})),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class PullRequestEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequest', graphql_name='node')


class PullRequestReviewCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReviewCommentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReviewComment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestReviewCommentEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestReviewComment', graphql_name='node')


class PullRequestReviewConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReviewEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReview'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestReviewContributionsByRepository(sgqlc.types.Type):
    __schema__ = github_schema
    contributions = sgqlc.types.Field(sgqlc.types.non_null(CreatedPullRequestReviewContributionConnection), graphql_name='contributions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ContributionOrder, graphql_name='orderBy', default={'field': 'OCCURRED_AT', 'direction': 'DESC'})),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class PullRequestReviewEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestReview', graphql_name='node')


class PullRequestReviewThreadConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReviewThreadEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestReviewThread'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestReviewThreadEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestReviewThread', graphql_name='node')


class PullRequestRevisionMarker(sgqlc.types.Type):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    last_seen_commit = sgqlc.types.Field(sgqlc.types.non_null('Commit'), graphql_name='lastSeenCommit')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')


class PullRequestTimelineConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestTimelineItemEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestTimelineItem'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PullRequestTimelineItemEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestTimelineItem', graphql_name='node')


class PullRequestTimelineItemsConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PullRequestTimelineItemsEdge'), graphql_name='edges')
    filtered_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='filteredCount')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PullRequestTimelineItems'), graphql_name='nodes')
    page_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pageCount')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class PullRequestTimelineItemsEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PullRequestTimelineItems', graphql_name='node')


class PushAllowanceConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('PushAllowanceEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('PushAllowance'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PushAllowanceEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('PushAllowance', graphql_name='node')


class Query(sgqlc.types.Type):
    __schema__ = github_schema
    code_of_conduct = sgqlc.types.Field('CodeOfConduct', graphql_name='codeOfConduct', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    codes_of_conduct = sgqlc.types.Field(sgqlc.types.list_of('CodeOfConduct'), graphql_name='codesOfConduct')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
        ('invitation_token', sgqlc.types.Arg(String, graphql_name='invitationToken', default=None)),
))
    )
    enterprise_administrator_invitation = sgqlc.types.Field('EnterpriseAdministratorInvitation', graphql_name='enterpriseAdministratorInvitation', args=sgqlc.types.ArgDict((
        ('user_login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='userLogin', default=None)),
        ('enterprise_slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='enterpriseSlug', default=None)),
        ('role', sgqlc.types.Arg(sgqlc.types.non_null(EnterpriseAdministratorRole), graphql_name='role', default=None)),
))
    )
    enterprise_administrator_invitation_by_token = sgqlc.types.Field('EnterpriseAdministratorInvitation', graphql_name='enterpriseAdministratorInvitationByToken', args=sgqlc.types.ArgDict((
        ('invitation_token', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='invitationToken', default=None)),
))
    )
    license = sgqlc.types.Field('License', graphql_name='license', args=sgqlc.types.ArgDict((
        ('key', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='key', default=None)),
))
    )
    licenses = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of('License')), graphql_name='licenses')
    marketplace_categories = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('MarketplaceCategory'))), graphql_name='marketplaceCategories', args=sgqlc.types.ArgDict((
        ('include_categories', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='includeCategories', default=None)),
        ('exclude_empty', sgqlc.types.Arg(Boolean, graphql_name='excludeEmpty', default=None)),
        ('exclude_subcategories', sgqlc.types.Arg(Boolean, graphql_name='excludeSubcategories', default=None)),
))
    )
    marketplace_category = sgqlc.types.Field('MarketplaceCategory', graphql_name='marketplaceCategory', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
        ('use_topic_aliases', sgqlc.types.Arg(Boolean, graphql_name='useTopicAliases', default=None)),
))
    )
    marketplace_listing = sgqlc.types.Field('MarketplaceListing', graphql_name='marketplaceListing', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
))
    )
    marketplace_listings = sgqlc.types.Field(sgqlc.types.non_null(MarketplaceListingConnection), graphql_name='marketplaceListings', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('category_slug', sgqlc.types.Arg(String, graphql_name='categorySlug', default=None)),
        ('use_topic_aliases', sgqlc.types.Arg(Boolean, graphql_name='useTopicAliases', default=None)),
        ('viewer_can_admin', sgqlc.types.Arg(Boolean, graphql_name='viewerCanAdmin', default=None)),
        ('admin_id', sgqlc.types.Arg(ID, graphql_name='adminId', default=None)),
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationId', default=None)),
        ('all_states', sgqlc.types.Arg(Boolean, graphql_name='allStates', default=None)),
        ('slugs', sgqlc.types.Arg(sgqlc.types.list_of(String), graphql_name='slugs', default=None)),
        ('primary_category_only', sgqlc.types.Arg(Boolean, graphql_name='primaryCategoryOnly', default=False)),
        ('with_free_trials_only', sgqlc.types.Arg(Boolean, graphql_name='withFreeTrialsOnly', default=False)),
))
    )
    meta = sgqlc.types.Field(sgqlc.types.non_null(GitHubMetadata), graphql_name='meta')
    node = sgqlc.types.Field(Node, graphql_name='node', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='id', default=None)),
))
    )
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Node)), graphql_name='nodes', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(ID))), graphql_name='ids', default=None)),
))
    )
    organization = sgqlc.types.Field('Organization', graphql_name='organization', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
))
    )
    rate_limit = sgqlc.types.Field('RateLimit', graphql_name='rateLimit', args=sgqlc.types.ArgDict((
        ('dry_run', sgqlc.types.Arg(Boolean, graphql_name='dryRun', default=False)),
))
    )
    relay = sgqlc.types.Field(sgqlc.types.non_null('Query'), graphql_name='relay')
    repository = sgqlc.types.Field('Repository', graphql_name='repository', args=sgqlc.types.ArgDict((
        ('owner', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='owner', default=None)),
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    repository_owner = sgqlc.types.Field('RepositoryOwner', graphql_name='repositoryOwner', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
))
    )
    resource = sgqlc.types.Field('UniformResourceLocatable', graphql_name='resource', args=sgqlc.types.ArgDict((
        ('url', sgqlc.types.Arg(sgqlc.types.non_null(URI), graphql_name='url', default=None)),
))
    )
    search = sgqlc.types.Field(sgqlc.types.non_null('SearchResultItemConnection'), graphql_name='search', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='query', default=None)),
        ('type', sgqlc.types.Arg(sgqlc.types.non_null(SearchType), graphql_name='type', default=None)),
))
    )
    security_advisories = sgqlc.types.Field(sgqlc.types.non_null('SecurityAdvisoryConnection'), graphql_name='securityAdvisories', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(SecurityAdvisoryOrder, graphql_name='orderBy', default={'field': 'UPDATED_AT', 'direction': 'DESC'})),
        ('identifier', sgqlc.types.Arg(SecurityAdvisoryIdentifierFilter, graphql_name='identifier', default=None)),
        ('published_since', sgqlc.types.Arg(DateTime, graphql_name='publishedSince', default=None)),
        ('updated_since', sgqlc.types.Arg(DateTime, graphql_name='updatedSince', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    security_advisory = sgqlc.types.Field('SecurityAdvisory', graphql_name='securityAdvisory', args=sgqlc.types.ArgDict((
        ('ghsa_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='ghsaId', default=None)),
))
    )
    security_vulnerabilities = sgqlc.types.Field(sgqlc.types.non_null('SecurityVulnerabilityConnection'), graphql_name='securityVulnerabilities', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(SecurityVulnerabilityOrder, graphql_name='orderBy', default={'field': 'UPDATED_AT', 'direction': 'DESC'})),
        ('ecosystem', sgqlc.types.Arg(SecurityAdvisoryEcosystem, graphql_name='ecosystem', default=None)),
        ('package', sgqlc.types.Arg(String, graphql_name='package', default=None)),
        ('severities', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SecurityAdvisorySeverity)), graphql_name='severities', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    topic = sgqlc.types.Field('Topic', graphql_name='topic', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    user = sgqlc.types.Field('User', graphql_name='user', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
))
    )
    viewer = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='viewer')


class RateLimit(sgqlc.types.Type):
    __schema__ = github_schema
    cost = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cost')
    limit = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='limit')
    node_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nodeCount')
    remaining = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='remaining')
    reset_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='resetAt')


class Reactable(sgqlc.types.Interface):
    __schema__ = github_schema
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ReactionGroup')), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null('ReactionConnection'), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')


class ReactingUserConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReactingUserEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReactingUserEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='node')
    reacted_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='reactedAt')


class ReactionConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReactionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Reaction'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    viewer_has_reacted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasReacted')


class ReactionEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Reaction', graphql_name='node')


class ReactionGroup(sgqlc.types.Type):
    __schema__ = github_schema
    content = sgqlc.types.Field(sgqlc.types.non_null(ReactionContent), graphql_name='content')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    subject = sgqlc.types.Field(sgqlc.types.non_null(Reactable), graphql_name='subject')
    users = sgqlc.types.Field(sgqlc.types.non_null(ReactingUserConnection), graphql_name='users', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    viewer_has_reacted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasReacted')


class RefConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('RefEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Ref'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RefEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Ref', graphql_name='node')


class RegenerateEnterpriseIdentityProviderRecoveryCodesPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    identity_provider = sgqlc.types.Field('EnterpriseIdentityProvider', graphql_name='identityProvider')


class RegistryPackageConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('RegistryPackageEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RegistryPackage'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RegistryPackageDependencyConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('RegistryPackageDependencyEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RegistryPackageDependency'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RegistryPackageDependencyEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RegistryPackageDependency', graphql_name='node')


class RegistryPackageEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RegistryPackage', graphql_name='node')


class RegistryPackageFileConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('RegistryPackageFileEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RegistryPackageFile'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RegistryPackageFileEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RegistryPackageFile', graphql_name='node')


class RegistryPackageOwner(sgqlc.types.Interface):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class RegistryPackageSearch(sgqlc.types.Interface):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class RegistryPackageStatistics(sgqlc.types.Type):
    __schema__ = github_schema


class RegistryPackageTagConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('RegistryPackageTagEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RegistryPackageTag'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RegistryPackageTagEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RegistryPackageTag', graphql_name='node')


class RegistryPackageVersionConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('RegistryPackageVersionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RegistryPackageVersion'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RegistryPackageVersionEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RegistryPackageVersion', graphql_name='node')


class RegistryPackageVersionStatistics(sgqlc.types.Type):
    __schema__ = github_schema


class ReleaseAssetConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReleaseAssetEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ReleaseAsset'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReleaseAssetEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ReleaseAsset', graphql_name='node')


class ReleaseConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReleaseEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Release'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReleaseEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Release', graphql_name='node')


class RemoveAssigneesFromAssignablePayload(sgqlc.types.Type):
    __schema__ = github_schema
    assignable = sgqlc.types.Field(Assignable, graphql_name='assignable')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class RemoveEnterpriseAdminPayload(sgqlc.types.Type):
    __schema__ = github_schema
    admin = sgqlc.types.Field('User', graphql_name='admin')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')
    viewer = sgqlc.types.Field('User', graphql_name='viewer')


class RemoveEnterpriseOrganizationPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    viewer = sgqlc.types.Field('User', graphql_name='viewer')


class RemoveLabelsFromLabelablePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    labelable = sgqlc.types.Field(Labelable, graphql_name='labelable')


class RemoveOutsideCollaboratorPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    removed_user = sgqlc.types.Field('User', graphql_name='removedUser')


class RemoveReactionPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    reaction = sgqlc.types.Field('Reaction', graphql_name='reaction')
    subject = sgqlc.types.Field(Reactable, graphql_name='subject')


class RemoveStarPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    starrable = sgqlc.types.Field('Starrable', graphql_name='starrable')


class ReopenIssuePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class ReopenPullRequestPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class RepositoryAuditEntryData(sgqlc.types.Interface):
    __schema__ = github_schema
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')


class RepositoryCollaboratorConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryCollaboratorEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryCollaboratorEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='node')
    permission = sgqlc.types.Field(sgqlc.types.non_null(RepositoryPermission), graphql_name='permission')
    permission_sources = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(PermissionSource)), graphql_name='permissionSources')


class RepositoryConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Repository'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    total_disk_usage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalDiskUsage')


class RepositoryEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Repository', graphql_name='node')


class RepositoryInfo(sgqlc.types.Interface):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='descriptionHTML')
    fork_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='forkCount')
    has_issues_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasIssuesEnabled')
    has_projects_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasProjectsEnabled')
    has_wiki_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasWikiEnabled')
    homepage_url = sgqlc.types.Field(URI, graphql_name='homepageUrl')
    is_archived = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isArchived')
    is_fork = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFork')
    is_locked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLocked')
    is_mirror = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMirror')
    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    is_template = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTemplate')
    license_info = sgqlc.types.Field('License', graphql_name='licenseInfo')
    lock_reason = sgqlc.types.Field(RepositoryLockReason, graphql_name='lockReason')
    mirror_url = sgqlc.types.Field(URI, graphql_name='mirrorUrl')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_with_owner = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nameWithOwner')
    open_graph_image_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='openGraphImageUrl')
    owner = sgqlc.types.Field(sgqlc.types.non_null('RepositoryOwner'), graphql_name='owner')
    pushed_at = sgqlc.types.Field(DateTime, graphql_name='pushedAt')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    short_description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='shortDescriptionHTML', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=200)),
))
    )
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    uses_custom_open_graph_image = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='usesCustomOpenGraphImage')


class RepositoryInvitationEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RepositoryInvitation', graphql_name='node')


class RepositoryNode(sgqlc.types.Interface):
    __schema__ = github_schema
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class RepositoryOwner(sgqlc.types.Interface):
    __schema__ = github_schema
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    repositories = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=['OWNER', 'COLLABORATOR'])),
        ('owner_affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='ownerAffiliations', default=['OWNER', 'COLLABORATOR'])),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('is_fork', sgqlc.types.Arg(Boolean, graphql_name='isFork', default=None)),
))
    )
    repository = sgqlc.types.Field('Repository', graphql_name='repository', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class RepositoryTopicConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryTopicEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RepositoryTopic'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryTopicEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RepositoryTopic', graphql_name='node')


class RepositoryVulnerabilityAlertConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('RepositoryVulnerabilityAlertEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('RepositoryVulnerabilityAlert'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class RepositoryVulnerabilityAlertEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('RepositoryVulnerabilityAlert', graphql_name='node')


class RequestReviewsPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')
    requested_reviewers_edge = sgqlc.types.Field('UserEdge', graphql_name='requestedReviewersEdge')


class ResolveReviewThreadPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    thread = sgqlc.types.Field('PullRequestReviewThread', graphql_name='thread')


class ReviewDismissalAllowanceConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReviewDismissalAllowanceEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ReviewDismissalAllowance'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReviewDismissalAllowanceEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ReviewDismissalAllowance', graphql_name='node')


class ReviewRequestConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('ReviewRequestEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('ReviewRequest'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ReviewRequestEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('ReviewRequest', graphql_name='node')


class SavedReplyConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('SavedReplyEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('SavedReply'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SavedReplyEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('SavedReply', graphql_name='node')


class SearchResultItemConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    code_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='codeCount')
    edges = sgqlc.types.Field(sgqlc.types.list_of('SearchResultItemEdge'), graphql_name='edges')
    issue_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='issueCount')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('SearchResultItem'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    repository_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='repositoryCount')
    user_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='userCount')
    wiki_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='wikiCount')


class SearchResultItemEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('SearchResultItem', graphql_name='node')
    text_matches = sgqlc.types.Field(sgqlc.types.list_of('TextMatch'), graphql_name='textMatches')


class SecurityAdvisoryConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('SecurityAdvisoryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('SecurityAdvisory'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SecurityAdvisoryEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('SecurityAdvisory', graphql_name='node')


class SecurityAdvisoryIdentifier(sgqlc.types.Type):
    __schema__ = github_schema
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')
    value = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='value')


class SecurityAdvisoryPackage(sgqlc.types.Type):
    __schema__ = github_schema
    ecosystem = sgqlc.types.Field(sgqlc.types.non_null(SecurityAdvisoryEcosystem), graphql_name='ecosystem')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class SecurityAdvisoryPackageVersion(sgqlc.types.Type):
    __schema__ = github_schema
    identifier = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='identifier')


class SecurityAdvisoryReference(sgqlc.types.Type):
    __schema__ = github_schema
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class SecurityVulnerability(sgqlc.types.Type):
    __schema__ = github_schema
    advisory = sgqlc.types.Field(sgqlc.types.non_null('SecurityAdvisory'), graphql_name='advisory')
    first_patched_version = sgqlc.types.Field(SecurityAdvisoryPackageVersion, graphql_name='firstPatchedVersion')
    package = sgqlc.types.Field(sgqlc.types.non_null(SecurityAdvisoryPackage), graphql_name='package')
    severity = sgqlc.types.Field(sgqlc.types.non_null(SecurityAdvisorySeverity), graphql_name='severity')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    vulnerable_version_range = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vulnerableVersionRange')


class SecurityVulnerabilityConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('SecurityVulnerabilityEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of(SecurityVulnerability), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SecurityVulnerabilityEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(SecurityVulnerability, graphql_name='node')


class Sponsorable(sgqlc.types.Interface):
    __schema__ = github_schema
    sponsors_listing = sgqlc.types.Field('SponsorsListing', graphql_name='sponsorsListing')
    sponsorships_as_maintainer = sgqlc.types.Field(sgqlc.types.non_null('SponsorshipConnection'), graphql_name='sponsorshipsAsMaintainer', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_private', sgqlc.types.Arg(Boolean, graphql_name='includePrivate', default=False)),
        ('order_by', sgqlc.types.Arg(SponsorshipOrder, graphql_name='orderBy', default=None)),
))
    )
    sponsorships_as_sponsor = sgqlc.types.Field(sgqlc.types.non_null('SponsorshipConnection'), graphql_name='sponsorshipsAsSponsor', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(SponsorshipOrder, graphql_name='orderBy', default=None)),
))
    )


class SponsorsTierAdminInfo(sgqlc.types.Type):
    __schema__ = github_schema
    sponsorships = sgqlc.types.Field(sgqlc.types.non_null('SponsorshipConnection'), graphql_name='sponsorships', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_private', sgqlc.types.Arg(Boolean, graphql_name='includePrivate', default=False)),
        ('order_by', sgqlc.types.Arg(SponsorshipOrder, graphql_name='orderBy', default=None)),
))
    )


class SponsorsTierConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('SponsorsTierEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('SponsorsTier'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SponsorsTierEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('SponsorsTier', graphql_name='node')


class SponsorshipConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('SponsorshipEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Sponsorship'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SponsorshipEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Sponsorship', graphql_name='node')


class StargazerConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('StargazerEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class StargazerEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='node')
    starred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='starredAt')


class Starrable(sgqlc.types.Interface):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    stargazers = sgqlc.types.Field(sgqlc.types.non_null(StargazerConnection), graphql_name='stargazers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(StarOrder, graphql_name='orderBy', default=None)),
))
    )
    viewer_has_starred = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasStarred')


class StarredRepositoryConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('StarredRepositoryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Repository'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class StarredRepositoryEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='node')
    starred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='starredAt')


class SubmitPullRequestReviewPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field('PullRequestReview', graphql_name='pullRequestReview')


class Subscribable(sgqlc.types.Interface):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    viewer_can_subscribe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSubscribe')
    viewer_subscription = sgqlc.types.Field(SubscriptionState, graphql_name='viewerSubscription')


class SuggestedReviewer(sgqlc.types.Type):
    __schema__ = github_schema
    is_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAuthor')
    is_commenter = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCommenter')
    reviewer = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='reviewer')


class TeamAuditEntryData(sgqlc.types.Interface):
    __schema__ = github_schema
    team = sgqlc.types.Field('Team', graphql_name='team')
    team_name = sgqlc.types.Field(String, graphql_name='teamName')
    team_resource_path = sgqlc.types.Field(URI, graphql_name='teamResourcePath')
    team_url = sgqlc.types.Field(URI, graphql_name='teamUrl')


class TeamConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('TeamEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Team'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TeamDiscussionCommentConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('TeamDiscussionCommentEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('TeamDiscussionComment'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TeamDiscussionCommentEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('TeamDiscussionComment', graphql_name='node')


class TeamDiscussionConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('TeamDiscussionEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('TeamDiscussion'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TeamDiscussionEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('TeamDiscussion', graphql_name='node')


class TeamEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Team', graphql_name='node')


class TeamMemberConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('TeamMemberEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TeamMemberEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    member_access_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='memberAccessResourcePath')
    member_access_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='memberAccessUrl')
    node = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='node')
    role = sgqlc.types.Field(sgqlc.types.non_null(TeamMemberRole), graphql_name='role')


class TeamRepositoryConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('TeamRepositoryEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Repository'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TeamRepositoryEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='node')
    permission = sgqlc.types.Field(sgqlc.types.non_null(RepositoryPermission), graphql_name='permission')


class TextMatch(sgqlc.types.Type):
    __schema__ = github_schema
    fragment = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fragment')
    highlights = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TextMatchHighlight'))), graphql_name='highlights')
    property = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='property')


class TextMatchHighlight(sgqlc.types.Type):
    __schema__ = github_schema
    begin_indice = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='beginIndice')
    end_indice = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='endIndice')
    text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='text')


class TopicAuditEntryData(sgqlc.types.Interface):
    __schema__ = github_schema
    topic = sgqlc.types.Field('Topic', graphql_name='topic')
    topic_name = sgqlc.types.Field(String, graphql_name='topicName')


class TopicConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('TopicEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('Topic'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TopicEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('Topic', graphql_name='node')


class TransferIssuePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class TreeEntry(sgqlc.types.Type):
    __schema__ = github_schema
    mode = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mode')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    object = sgqlc.types.Field(GitObject, graphql_name='object')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='type')


class UnarchiveRepositoryPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class UnfollowUserPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user = sgqlc.types.Field('User', graphql_name='user')


class UniformResourceLocatable(sgqlc.types.Interface):
    __schema__ = github_schema
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class UnlinkRepositoryFromProjectPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field('Project', graphql_name='project')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class UnlockLockablePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    unlocked_record = sgqlc.types.Field(Lockable, graphql_name='unlockedRecord')


class UnmarkIssueAsDuplicatePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    duplicate = sgqlc.types.Field('IssueOrPullRequest', graphql_name='duplicate')


class UnresolveReviewThreadPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    thread = sgqlc.types.Field('PullRequestReviewThread', graphql_name='thread')


class Updatable(sgqlc.types.Interface):
    __schema__ = github_schema
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')


class UpdatableComment(sgqlc.types.Interface):
    __schema__ = github_schema
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')


class UpdateBranchProtectionRulePayload(sgqlc.types.Type):
    __schema__ = github_schema
    branch_protection_rule = sgqlc.types.Field('BranchProtectionRule', graphql_name='branchProtectionRule')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateEnterpriseActionExecutionCapabilitySettingPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseAdministratorRolePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseAllowPrivateRepositoryForkingSettingPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseDefaultRepositoryPermissionSettingPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanChangeRepositoryVisibilitySettingPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanCreateRepositoriesSettingPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanDeleteIssuesSettingPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanDeleteRepositoriesSettingPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanInviteCollaboratorsSettingPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanMakePurchasesSettingPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanUpdateProtectedBranchesSettingPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseMembersCanViewDependencyInsightsSettingPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseOrganizationProjectsSettingPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseProfilePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')


class UpdateEnterpriseRepositoryProjectsSettingPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseTeamDiscussionsSettingPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateEnterpriseTwoFactorAuthenticationRequiredSettingPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    enterprise = sgqlc.types.Field('Enterprise', graphql_name='enterprise')
    message = sgqlc.types.Field(String, graphql_name='message')


class UpdateIssueCommentPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue_comment = sgqlc.types.Field('IssueComment', graphql_name='issueComment')


class UpdateIssuePayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    issue = sgqlc.types.Field('Issue', graphql_name='issue')


class UpdateProjectCardPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_card = sgqlc.types.Field('ProjectCard', graphql_name='projectCard')


class UpdateProjectColumnPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project_column = sgqlc.types.Field('ProjectColumn', graphql_name='projectColumn')


class UpdateProjectPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    project = sgqlc.types.Field('Project', graphql_name='project')


class UpdatePullRequestPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')


class UpdatePullRequestReviewCommentPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review_comment = sgqlc.types.Field('PullRequestReviewComment', graphql_name='pullRequestReviewComment')


class UpdatePullRequestReviewPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    pull_request_review = sgqlc.types.Field('PullRequestReview', graphql_name='pullRequestReview')


class UpdateRefPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ref = sgqlc.types.Field('Ref', graphql_name='ref')


class UpdateRepositoryPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class UpdateSubscriptionPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subscribable = sgqlc.types.Field(Subscribable, graphql_name='subscribable')


class UpdateTeamDiscussionCommentPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    team_discussion_comment = sgqlc.types.Field('TeamDiscussionComment', graphql_name='teamDiscussionComment')


class UpdateTeamDiscussionPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    team_discussion = sgqlc.types.Field('TeamDiscussion', graphql_name='teamDiscussion')


class UpdateTopicsPayload(sgqlc.types.Type):
    __schema__ = github_schema
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invalid_topic_names = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='invalidTopicNames')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')


class UserConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('User'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserContentEditConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserContentEditEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('UserContentEdit'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserContentEditEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('UserContentEdit', graphql_name='node')


class UserEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('User', graphql_name='node')


class UserStatusConnection(sgqlc.types.relay.Connection):
    __schema__ = github_schema
    edges = sgqlc.types.Field(sgqlc.types.list_of('UserStatusEdge'), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('UserStatus'), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserStatusEdge(sgqlc.types.Type):
    __schema__ = github_schema
    cursor = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='cursor')
    node = sgqlc.types.Field('UserStatus', graphql_name='node')


class AddedToProjectEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class App(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    logo_background_color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='logoBackgroundColor')
    logo_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='logoUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class AssignedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    assignable = sgqlc.types.Field(sgqlc.types.non_null(Assignable), graphql_name='assignable')
    assignee = sgqlc.types.Field('Assignee', graphql_name='assignee')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class BaseRefChangedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class BaseRefForcePushedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    after_commit = sgqlc.types.Field('Commit', graphql_name='afterCommit')
    before_commit = sgqlc.types.Field('Commit', graphql_name='beforeCommit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')
    ref = sgqlc.types.Field('Ref', graphql_name='ref')


class Blob(sgqlc.types.Type, Node, GitObject):
    __schema__ = github_schema
    abbreviated_oid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='abbreviatedOid')
    byte_size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='byteSize')
    commit_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitResourcePath')
    commit_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_binary = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBinary')
    is_truncated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTruncated')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    text = sgqlc.types.Field(String, graphql_name='text')


class Bot(sgqlc.types.Type, Node, Actor, UniformResourceLocatable):
    __schema__ = github_schema
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class BranchProtectionRule(sgqlc.types.Type, Node):
    __schema__ = github_schema
    branch_protection_rule_conflicts = sgqlc.types.Field(sgqlc.types.non_null(BranchProtectionRuleConflictConnection), graphql_name='branchProtectionRuleConflicts', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    dismisses_stale_reviews = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='dismissesStaleReviews')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_admin_enforced = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdminEnforced')
    matching_refs = sgqlc.types.Field(sgqlc.types.non_null(RefConnection), graphql_name='matchingRefs', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pattern')
    push_allowances = sgqlc.types.Field(sgqlc.types.non_null(PushAllowanceConnection), graphql_name='pushAllowances', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    required_approving_review_count = sgqlc.types.Field(Int, graphql_name='requiredApprovingReviewCount')
    required_status_check_contexts = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='requiredStatusCheckContexts')
    requires_approving_reviews = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresApprovingReviews')
    requires_code_owner_reviews = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresCodeOwnerReviews')
    requires_commit_signatures = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresCommitSignatures')
    requires_status_checks = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresStatusChecks')
    requires_strict_status_checks = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='requiresStrictStatusChecks')
    restricts_pushes = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restrictsPushes')
    restricts_review_dismissals = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='restrictsReviewDismissals')
    review_dismissal_allowances = sgqlc.types.Field(sgqlc.types.non_null(ReviewDismissalAllowanceConnection), graphql_name='reviewDismissalAllowances', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class ClosedEvent(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    closable = sgqlc.types.Field(sgqlc.types.non_null(Closable), graphql_name='closable')
    closer = sgqlc.types.Field('Closer', graphql_name='closer')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class CodeOfConduct(sgqlc.types.Type, Node):
    __schema__ = github_schema
    body = sgqlc.types.Field(String, graphql_name='body')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    resource_path = sgqlc.types.Field(URI, graphql_name='resourcePath')
    url = sgqlc.types.Field(URI, graphql_name='url')


class CommentDeletedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class Commit(sgqlc.types.Type, Node, GitObject, Subscribable, UniformResourceLocatable):
    __schema__ = github_schema
    abbreviated_oid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='abbreviatedOid')
    additions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='additions')
    associated_pull_requests = sgqlc.types.Field(PullRequestConnection, graphql_name='associatedPullRequests', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(PullRequestOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'ASC'})),
))
    )
    author = sgqlc.types.Field(GitActor, graphql_name='author')
    authored_by_committer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='authoredByCommitter')
    authored_date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='authoredDate')
    blame = sgqlc.types.Field(sgqlc.types.non_null(Blame), graphql_name='blame', args=sgqlc.types.ArgDict((
        ('path', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='path', default=None)),
))
    )
    changed_files = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='changedFiles')
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommitCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    commit_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitResourcePath')
    commit_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitUrl')
    committed_date = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='committedDate')
    committed_via_web = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='committedViaWeb')
    committer = sgqlc.types.Field(GitActor, graphql_name='committer')
    deletions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='deletions')
    deployments = sgqlc.types.Field(DeploymentConnection, graphql_name='deployments', args=sgqlc.types.ArgDict((
        ('environments', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='environments', default=None)),
        ('order_by', sgqlc.types.Arg(DeploymentOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    history = sgqlc.types.Field(sgqlc.types.non_null(CommitHistoryConnection), graphql_name='history', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('path', sgqlc.types.Arg(String, graphql_name='path', default=None)),
        ('author', sgqlc.types.Arg(CommitAuthor, graphql_name='author', default=None)),
        ('since', sgqlc.types.Arg(GitTimestamp, graphql_name='since', default=None)),
        ('until', sgqlc.types.Arg(GitTimestamp, graphql_name='until', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    message_body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='messageBody')
    message_body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='messageBodyHTML')
    message_headline = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='messageHeadline')
    message_headline_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='messageHeadlineHTML')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    parents = sgqlc.types.Field(sgqlc.types.non_null(CommitConnection), graphql_name='parents', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pushed_date = sgqlc.types.Field(DateTime, graphql_name='pushedDate')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    signature = sgqlc.types.Field(GitSignature, graphql_name='signature')
    status = sgqlc.types.Field('Status', graphql_name='status')
    tarball_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='tarballUrl')
    tree = sgqlc.types.Field(sgqlc.types.non_null('Tree'), graphql_name='tree')
    tree_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='treeResourcePath')
    tree_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='treeUrl')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_subscribe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSubscribe')
    viewer_subscription = sgqlc.types.Field(SubscriptionState, graphql_name='viewerSubscription')
    zipball_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='zipballUrl')


class CommitComment(sgqlc.types.Type, Node, Comment, Deletable, Updatable, UpdatableComment, Reactable, RepositoryNode):
    __schema__ = github_schema
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    includes_created_edit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includesCreatedEdit')
    is_minimized = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMinimized')
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    minimized_reason = sgqlc.types.Field(String, graphql_name='minimizedReason')
    path = sgqlc.types.Field(String, graphql_name='path')
    position = sgqlc.types.Field(Int, graphql_name='position')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ReactionGroup)), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(ReactionConnection), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    viewer_can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelete')
    viewer_can_minimize = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanMinimize')
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')


class CommitCommentThread(sgqlc.types.Type, Node, RepositoryNode):
    __schema__ = github_schema
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommitCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    path = sgqlc.types.Field(String, graphql_name='path')
    position = sgqlc.types.Field(Int, graphql_name='position')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class ConvertedNoteToIssueEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class CreatedCommitContribution(sgqlc.types.Type, Contribution):
    __schema__ = github_schema
    commit_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='commitCount')
    is_restricted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRestricted')
    occurred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='occurredAt')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')


class CreatedIssueContribution(sgqlc.types.Type, Contribution):
    __schema__ = github_schema
    is_restricted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRestricted')
    issue = sgqlc.types.Field(sgqlc.types.non_null('Issue'), graphql_name='issue')
    occurred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='occurredAt')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')


class CreatedPullRequestContribution(sgqlc.types.Type, Contribution):
    __schema__ = github_schema
    is_restricted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRestricted')
    occurred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='occurredAt')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')


class CreatedPullRequestReviewContribution(sgqlc.types.Type, Contribution):
    __schema__ = github_schema
    is_restricted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRestricted')
    occurred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='occurredAt')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')
    pull_request_review = sgqlc.types.Field(sgqlc.types.non_null('PullRequestReview'), graphql_name='pullRequestReview')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')


class CreatedRepositoryContribution(sgqlc.types.Type, Contribution):
    __schema__ = github_schema
    is_restricted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRestricted')
    occurred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='occurredAt')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')


class CrossReferencedEvent(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_cross_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCrossRepository')
    referenced_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='referencedAt')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    source = sgqlc.types.Field(sgqlc.types.non_null('ReferencedSubject'), graphql_name='source')
    target = sgqlc.types.Field(sgqlc.types.non_null('ReferencedSubject'), graphql_name='target')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    will_close_target = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='willCloseTarget')


class DemilestonedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    milestone_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='milestoneTitle')
    subject = sgqlc.types.Field(sgqlc.types.non_null('MilestoneItem'), graphql_name='subject')


class DeployKey(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    read_only = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='readOnly')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='verified')


class DeployedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    deployment = sgqlc.types.Field(sgqlc.types.non_null('Deployment'), graphql_name='deployment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')
    ref = sgqlc.types.Field('Ref', graphql_name='ref')


class Deployment(sgqlc.types.Type, Node):
    __schema__ = github_schema
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    commit_oid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='commitOid')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    description = sgqlc.types.Field(String, graphql_name='description')
    environment = sgqlc.types.Field(String, graphql_name='environment')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    latest_status = sgqlc.types.Field('DeploymentStatus', graphql_name='latestStatus')
    payload = sgqlc.types.Field(String, graphql_name='payload')
    ref = sgqlc.types.Field('Ref', graphql_name='ref')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    state = sgqlc.types.Field(DeploymentState, graphql_name='state')
    statuses = sgqlc.types.Field(DeploymentStatusConnection, graphql_name='statuses', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    task = sgqlc.types.Field(String, graphql_name='task')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class DeploymentEnvironmentChangedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    deployment_status = sgqlc.types.Field(sgqlc.types.non_null('DeploymentStatus'), graphql_name='deploymentStatus')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')


class DeploymentStatus(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    deployment = sgqlc.types.Field(sgqlc.types.non_null(Deployment), graphql_name='deployment')
    description = sgqlc.types.Field(String, graphql_name='description')
    environment_url = sgqlc.types.Field(URI, graphql_name='environmentUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    log_url = sgqlc.types.Field(URI, graphql_name='logUrl')
    state = sgqlc.types.Field(sgqlc.types.non_null(DeploymentStatusState), graphql_name='state')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class Enterprise(sgqlc.types.Type, Node):
    __schema__ = github_schema
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    billing_info = sgqlc.types.Field(EnterpriseBillingInfo, graphql_name='billingInfo')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='descriptionHTML')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    location = sgqlc.types.Field(String, graphql_name='location')
    members = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseMemberConnection), graphql_name='members', args=sgqlc.types.ArgDict((
        ('organization_logins', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='organizationLogins', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(EnterpriseMemberOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
        ('role', sgqlc.types.Arg(EnterpriseUserAccountMembershipRole, graphql_name='role', default=None)),
        ('deployment', sgqlc.types.Arg(EnterpriseUserDeployment, graphql_name='deployment', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    organizations = sgqlc.types.Field(sgqlc.types.non_null(OrganizationConnection), graphql_name='organizations', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    owner_info = sgqlc.types.Field(EnterpriseOwnerInfo, graphql_name='ownerInfo')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_accounts = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseUserAccountConnection), graphql_name='userAccounts', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    viewer_is_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerIsAdmin')
    website_url = sgqlc.types.Field(URI, graphql_name='websiteUrl')


class EnterpriseAdministratorInvitation(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    email = sgqlc.types.Field(String, graphql_name='email')
    enterprise = sgqlc.types.Field(sgqlc.types.non_null(Enterprise), graphql_name='enterprise')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    invitee = sgqlc.types.Field('User', graphql_name='invitee')
    inviter = sgqlc.types.Field('User', graphql_name='inviter')
    role = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseAdministratorRole), graphql_name='role')


class EnterpriseIdentityProvider(sgqlc.types.Type, Node):
    __schema__ = github_schema
    digest_method = sgqlc.types.Field(SamlDigestAlgorithm, graphql_name='digestMethod')
    enterprise = sgqlc.types.Field(Enterprise, graphql_name='enterprise')
    external_identities = sgqlc.types.Field(sgqlc.types.non_null(ExternalIdentityConnection), graphql_name='externalIdentities', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    idp_certificate = sgqlc.types.Field(X509Certificate, graphql_name='idpCertificate')
    issuer = sgqlc.types.Field(String, graphql_name='issuer')
    recovery_codes = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='recoveryCodes')
    signature_method = sgqlc.types.Field(SamlSignatureAlgorithm, graphql_name='signatureMethod')
    sso_url = sgqlc.types.Field(URI, graphql_name='ssoUrl')


class EnterpriseRepositoryInfo(sgqlc.types.Type, Node):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_with_owner = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nameWithOwner')


class EnterpriseServerInstallation(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    customer_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='customerName')
    host_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='hostName')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_connected = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isConnected')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    user_accounts = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccountConnection), graphql_name='userAccounts', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(EnterpriseServerUserAccountOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    user_accounts_uploads = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccountsUploadConnection), graphql_name='userAccountsUploads', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(EnterpriseServerUserAccountsUploadOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'DESC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class EnterpriseServerUserAccount(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    emails = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccountEmailConnection), graphql_name='emails', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(EnterpriseServerUserAccountEmailOrder, graphql_name='orderBy', default={'field': 'EMAIL', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    enterprise_server_installation = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerInstallation), graphql_name='enterpriseServerInstallation')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_site_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSiteAdmin')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    profile_name = sgqlc.types.Field(String, graphql_name='profileName')
    remote_created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='remoteCreatedAt')
    remote_user_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='remoteUserId')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class EnterpriseServerUserAccountEmail(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_primary = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrimary')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    user_account = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccount), graphql_name='userAccount')


class EnterpriseServerUserAccountsUpload(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    enterprise = sgqlc.types.Field(sgqlc.types.non_null(Enterprise), graphql_name='enterprise')
    enterprise_server_installation = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerInstallation), graphql_name='enterpriseServerInstallation')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    sync_state = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseServerUserAccountsUploadSyncState), graphql_name='syncState')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class EnterpriseUserAccount(sgqlc.types.Type, Node, Actor):
    __schema__ = github_schema
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    enterprise = sgqlc.types.Field(sgqlc.types.non_null(Enterprise), graphql_name='enterprise')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    name = sgqlc.types.Field(String, graphql_name='name')
    organizations = sgqlc.types.Field(sgqlc.types.non_null(EnterpriseOrganizationMembershipConnection), graphql_name='organizations', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(OrganizationOrder, graphql_name='orderBy', default={'field': 'LOGIN', 'direction': 'ASC'})),
        ('role', sgqlc.types.Arg(EnterpriseUserAccountMembershipRole, graphql_name='role', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user = sgqlc.types.Field('User', graphql_name='user')


class ExternalIdentity(sgqlc.types.Type, Node):
    __schema__ = github_schema
    guid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='guid')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    organization_invitation = sgqlc.types.Field('OrganizationInvitation', graphql_name='organizationInvitation')
    saml_identity = sgqlc.types.Field(ExternalIdentitySamlAttributes, graphql_name='samlIdentity')
    scim_identity = sgqlc.types.Field(ExternalIdentityScimAttributes, graphql_name='scimIdentity')
    user = sgqlc.types.Field('User', graphql_name='user')


class GenericHovercardContext(sgqlc.types.Type, HovercardContext):
    __schema__ = github_schema
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    octicon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='octicon')


class Gist(sgqlc.types.Type, Node, Starrable, UniformResourceLocatable):
    __schema__ = github_schema
    comments = sgqlc.types.Field(sgqlc.types.non_null(GistCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    files = sgqlc.types.Field(sgqlc.types.list_of(GistFile), graphql_name='files', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=10)),
        ('oid', sgqlc.types.Arg(GitObjectID, graphql_name='oid', default=None)),
))
    )
    forks = sgqlc.types.Field(sgqlc.types.non_null(GistConnection), graphql_name='forks', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(GistOrder, graphql_name='orderBy', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_fork = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFork')
    is_public = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublic')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    owner = sgqlc.types.Field(RepositoryOwner, graphql_name='owner')
    pushed_at = sgqlc.types.Field(DateTime, graphql_name='pushedAt')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    stargazers = sgqlc.types.Field(sgqlc.types.non_null(StargazerConnection), graphql_name='stargazers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(StarOrder, graphql_name='orderBy', default=None)),
))
    )
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_has_starred = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasStarred')


class GistComment(sgqlc.types.Type, Node, Comment, Deletable, Updatable, UpdatableComment):
    __schema__ = github_schema
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    gist = sgqlc.types.Field(sgqlc.types.non_null(Gist), graphql_name='gist')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    includes_created_edit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includesCreatedEdit')
    is_minimized = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMinimized')
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    minimized_reason = sgqlc.types.Field(String, graphql_name='minimizedReason')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    viewer_can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelete')
    viewer_can_minimize = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanMinimize')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')


class GpgSignature(sgqlc.types.Type, GitSignature):
    __schema__ = github_schema
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    is_valid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isValid')
    key_id = sgqlc.types.Field(String, graphql_name='keyId')
    payload = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='payload')
    signature = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='signature')
    signer = sgqlc.types.Field('User', graphql_name='signer')
    state = sgqlc.types.Field(sgqlc.types.non_null(GitSignatureState), graphql_name='state')
    was_signed_by_git_hub = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='wasSignedByGitHub')


class HeadRefDeletedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    head_ref = sgqlc.types.Field('Ref', graphql_name='headRef')
    head_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='headRefName')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')


class HeadRefForcePushedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    after_commit = sgqlc.types.Field(Commit, graphql_name='afterCommit')
    before_commit = sgqlc.types.Field(Commit, graphql_name='beforeCommit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')
    ref = sgqlc.types.Field('Ref', graphql_name='ref')


class HeadRefRestoredEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')


class Issue(sgqlc.types.Type, Node, Assignable, Closable, Comment, Updatable, UpdatableComment, Labelable, Lockable, Reactable, RepositoryNode, Subscribable, UniformResourceLocatable):
    __schema__ = github_schema
    active_lock_reason = sgqlc.types.Field(LockReason, graphql_name='activeLockReason')
    assignees = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='assignees', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    closed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='closed')
    closed_at = sgqlc.types.Field(DateTime, graphql_name='closedAt')
    comments = sgqlc.types.Field(sgqlc.types.non_null(IssueCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    hovercard = sgqlc.types.Field(sgqlc.types.non_null(Hovercard), graphql_name='hovercard', args=sgqlc.types.ArgDict((
        ('include_notification_contexts', sgqlc.types.Arg(Boolean, graphql_name='includeNotificationContexts', default=True)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    includes_created_edit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includesCreatedEdit')
    labels = sgqlc.types.Field(LabelConnection, graphql_name='labels', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    locked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='locked')
    milestone = sgqlc.types.Field('Milestone', graphql_name='milestone')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    participants = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='participants', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    project_cards = sgqlc.types.Field(sgqlc.types.non_null(ProjectCardConnection), graphql_name='projectCards', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('archived_states', sgqlc.types.Arg(sgqlc.types.list_of(ProjectCardArchivedState), graphql_name='archivedStates', default=['ARCHIVED', 'NOT_ARCHIVED'])),
))
    )
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ReactionGroup)), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(ReactionConnection), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    state = sgqlc.types.Field(sgqlc.types.non_null(IssueState), graphql_name='state')
    timeline_items = sgqlc.types.Field(sgqlc.types.non_null(IssueTimelineItemsConnection), graphql_name='timelineItems', args=sgqlc.types.ArgDict((
        ('since', sgqlc.types.Arg(DateTime, graphql_name='since', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('item_types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueTimelineItemsItemType)), graphql_name='itemTypes', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')
    viewer_can_subscribe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSubscribe')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')
    viewer_subscription = sgqlc.types.Field(SubscriptionState, graphql_name='viewerSubscription')


class IssueComment(sgqlc.types.Type, Node, Comment, Deletable, Updatable, UpdatableComment, Reactable, RepositoryNode):
    __schema__ = github_schema
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    includes_created_edit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includesCreatedEdit')
    is_minimized = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMinimized')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    minimized_reason = sgqlc.types.Field(String, graphql_name='minimizedReason')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    pull_request = sgqlc.types.Field('PullRequest', graphql_name='pullRequest')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ReactionGroup)), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(ReactionConnection), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    viewer_can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelete')
    viewer_can_minimize = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanMinimize')
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')


class JoinedGitHubContribution(sgqlc.types.Type, Contribution):
    __schema__ = github_schema
    is_restricted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRestricted')
    occurred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='occurredAt')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')


class Label(sgqlc.types.Type, Node):
    __schema__ = github_schema
    color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='color')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_default = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefault')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='states', default=None)),
        ('filter_by', sgqlc.types.Arg(IssueFilters, graphql_name='filterBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    pull_requests = sgqlc.types.Field(sgqlc.types.non_null(PullRequestConnection), graphql_name='pullRequests', args=sgqlc.types.ArgDict((
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class LabeledEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    label = sgqlc.types.Field(sgqlc.types.non_null(Label), graphql_name='label')
    labelable = sgqlc.types.Field(sgqlc.types.non_null(Labelable), graphql_name='labelable')


class Language(sgqlc.types.Type, Node):
    __schema__ = github_schema
    color = sgqlc.types.Field(String, graphql_name='color')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')


class License(sgqlc.types.Type, Node):
    __schema__ = github_schema
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    conditions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(LicenseRule)), graphql_name='conditions')
    description = sgqlc.types.Field(String, graphql_name='description')
    featured = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='featured')
    hidden = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hidden')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    implementation = sgqlc.types.Field(String, graphql_name='implementation')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    limitations = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(LicenseRule)), graphql_name='limitations')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    nickname = sgqlc.types.Field(String, graphql_name='nickname')
    permissions = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(LicenseRule)), graphql_name='permissions')
    pseudo_license = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='pseudoLicense')
    spdx_id = sgqlc.types.Field(String, graphql_name='spdxId')
    url = sgqlc.types.Field(URI, graphql_name='url')


class LockedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    lock_reason = sgqlc.types.Field(LockReason, graphql_name='lockReason')
    lockable = sgqlc.types.Field(sgqlc.types.non_null(Lockable), graphql_name='lockable')


class Mannequin(sgqlc.types.Type, Node, Actor, UniformResourceLocatable):
    __schema__ = github_schema
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class MarkedAsDuplicateEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class MarketplaceCategory(sgqlc.types.Type, Node):
    __schema__ = github_schema
    description = sgqlc.types.Field(String, graphql_name='description')
    how_it_works = sgqlc.types.Field(String, graphql_name='howItWorks')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    primary_listing_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='primaryListingCount')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    secondary_listing_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='secondaryListingCount')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class MarketplaceListing(sgqlc.types.Type, Node):
    __schema__ = github_schema
    app = sgqlc.types.Field(App, graphql_name='app')
    company_url = sgqlc.types.Field(URI, graphql_name='companyUrl')
    configuration_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='configurationResourcePath')
    configuration_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='configurationUrl')
    documentation_url = sgqlc.types.Field(URI, graphql_name='documentationUrl')
    extended_description = sgqlc.types.Field(String, graphql_name='extendedDescription')
    extended_description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='extendedDescriptionHTML')
    full_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullDescription')
    full_description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='fullDescriptionHTML')
    has_published_free_trial_plans = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPublishedFreeTrialPlans')
    has_terms_of_service = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasTermsOfService')
    how_it_works = sgqlc.types.Field(String, graphql_name='howItWorks')
    how_it_works_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='howItWorksHTML')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    installation_url = sgqlc.types.Field(URI, graphql_name='installationUrl')
    installed_for_viewer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='installedForViewer')
    is_archived = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isArchived')
    is_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDraft')
    is_paid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPaid')
    is_public = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPublic')
    is_rejected = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRejected')
    is_unverified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUnverified')
    is_unverified_pending = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isUnverifiedPending')
    is_verification_pending_from_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVerificationPendingFromDraft')
    is_verification_pending_from_unverified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVerificationPendingFromUnverified')
    is_verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVerified')
    logo_background_color = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='logoBackgroundColor')
    logo_url = sgqlc.types.Field(URI, graphql_name='logoUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=400)),
))
    )
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    normalized_short_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='normalizedShortDescription')
    pricing_url = sgqlc.types.Field(URI, graphql_name='pricingUrl')
    primary_category = sgqlc.types.Field(sgqlc.types.non_null(MarketplaceCategory), graphql_name='primaryCategory')
    privacy_policy_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='privacyPolicyUrl')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    screenshot_urls = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(String)), graphql_name='screenshotUrls')
    secondary_category = sgqlc.types.Field(MarketplaceCategory, graphql_name='secondaryCategory')
    short_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shortDescription')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    status_url = sgqlc.types.Field(URI, graphql_name='statusUrl')
    support_email = sgqlc.types.Field(String, graphql_name='supportEmail')
    support_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='supportUrl')
    terms_of_service_url = sgqlc.types.Field(URI, graphql_name='termsOfServiceUrl')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_add_plans = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanAddPlans')
    viewer_can_approve = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanApprove')
    viewer_can_delist = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelist')
    viewer_can_edit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanEdit')
    viewer_can_edit_categories = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanEditCategories')
    viewer_can_edit_plans = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanEditPlans')
    viewer_can_redraft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanRedraft')
    viewer_can_reject = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReject')
    viewer_can_request_approval = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanRequestApproval')
    viewer_has_purchased = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasPurchased')
    viewer_has_purchased_for_all_organizations = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasPurchasedForAllOrganizations')
    viewer_is_listing_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerIsListingAdmin')


class MembersCanDeleteReposClearAuditEntry(sgqlc.types.Type, Node, AuditEntry, EnterpriseAuditEntryData, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    enterprise_resource_path = sgqlc.types.Field(URI, graphql_name='enterpriseResourcePath')
    enterprise_slug = sgqlc.types.Field(String, graphql_name='enterpriseSlug')
    enterprise_url = sgqlc.types.Field(URI, graphql_name='enterpriseUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class MembersCanDeleteReposDisableAuditEntry(sgqlc.types.Type, Node, AuditEntry, EnterpriseAuditEntryData, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    enterprise_resource_path = sgqlc.types.Field(URI, graphql_name='enterpriseResourcePath')
    enterprise_slug = sgqlc.types.Field(String, graphql_name='enterpriseSlug')
    enterprise_url = sgqlc.types.Field(URI, graphql_name='enterpriseUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class MembersCanDeleteReposEnableAuditEntry(sgqlc.types.Type, Node, AuditEntry, EnterpriseAuditEntryData, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    enterprise_resource_path = sgqlc.types.Field(URI, graphql_name='enterpriseResourcePath')
    enterprise_slug = sgqlc.types.Field(String, graphql_name='enterpriseSlug')
    enterprise_url = sgqlc.types.Field(URI, graphql_name='enterpriseUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class MentionedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class MergedEvent(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    merge_ref = sgqlc.types.Field('Ref', graphql_name='mergeRef')
    merge_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='mergeRefName')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null('PullRequest'), graphql_name='pullRequest')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class Milestone(sgqlc.types.Type, Node, Closable, UniformResourceLocatable):
    __schema__ = github_schema
    closed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='closed')
    closed_at = sgqlc.types.Field(DateTime, graphql_name='closedAt')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    description = sgqlc.types.Field(String, graphql_name='description')
    due_on = sgqlc.types.Field(DateTime, graphql_name='dueOn')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    issue_priorities_debug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='issuePrioritiesDebug')
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='states', default=None)),
        ('filter_by', sgqlc.types.Arg(IssueFilters, graphql_name='filterBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    pull_requests = sgqlc.types.Field(sgqlc.types.non_null(PullRequestConnection), graphql_name='pullRequests', args=sgqlc.types.ArgDict((
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    state = sgqlc.types.Field(sgqlc.types.non_null(MilestoneState), graphql_name='state')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class MilestonedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    milestone_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='milestoneTitle')
    subject = sgqlc.types.Field(sgqlc.types.non_null('MilestoneItem'), graphql_name='subject')


class MovedColumnsInProjectEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class OauthApplicationCreateAuditEntry(sgqlc.types.Type, Node, AuditEntry, OauthApplicationAuditEntryData, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    application_url = sgqlc.types.Field(URI, graphql_name='applicationUrl')
    callback_url = sgqlc.types.Field(URI, graphql_name='callbackUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    oauth_application_name = sgqlc.types.Field(String, graphql_name='oauthApplicationName')
    oauth_application_resource_path = sgqlc.types.Field(URI, graphql_name='oauthApplicationResourcePath')
    oauth_application_url = sgqlc.types.Field(URI, graphql_name='oauthApplicationUrl')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    rate_limit = sgqlc.types.Field(Int, graphql_name='rateLimit')
    state = sgqlc.types.Field(OauthApplicationCreateAuditEntryState, graphql_name='state')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgAddBillingManagerAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    invitation_email = sgqlc.types.Field(String, graphql_name='invitationEmail')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgAddMemberAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    permission = sgqlc.types.Field(OrgAddMemberAuditEntryPermission, graphql_name='permission')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgBlockUserAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    blocked_user = sgqlc.types.Field('User', graphql_name='blockedUser')
    blocked_user_name = sgqlc.types.Field(String, graphql_name='blockedUserName')
    blocked_user_resource_path = sgqlc.types.Field(URI, graphql_name='blockedUserResourcePath')
    blocked_user_url = sgqlc.types.Field(URI, graphql_name='blockedUserUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgConfigDisableCollaboratorsOnlyAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgConfigEnableCollaboratorsOnlyAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgCreateAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    billing_plan = sgqlc.types.Field(OrgCreateAuditEntryBillingPlan, graphql_name='billingPlan')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgDisableOauthAppRestrictionsAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgDisableSamlAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    digest_method_url = sgqlc.types.Field(URI, graphql_name='digestMethodUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    issuer_url = sgqlc.types.Field(URI, graphql_name='issuerUrl')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    signature_method_url = sgqlc.types.Field(URI, graphql_name='signatureMethodUrl')
    single_sign_on_url = sgqlc.types.Field(URI, graphql_name='singleSignOnUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgDisableTwoFactorRequirementAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgEnableOauthAppRestrictionsAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgEnableSamlAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    digest_method_url = sgqlc.types.Field(URI, graphql_name='digestMethodUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    issuer_url = sgqlc.types.Field(URI, graphql_name='issuerUrl')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    signature_method_url = sgqlc.types.Field(URI, graphql_name='signatureMethodUrl')
    single_sign_on_url = sgqlc.types.Field(URI, graphql_name='singleSignOnUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgEnableTwoFactorRequirementAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgInviteMemberAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_invitation = sgqlc.types.Field('OrganizationInvitation', graphql_name='organizationInvitation')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgInviteToBusinessAuditEntry(sgqlc.types.Type, Node, AuditEntry, EnterpriseAuditEntryData, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    enterprise_resource_path = sgqlc.types.Field(URI, graphql_name='enterpriseResourcePath')
    enterprise_slug = sgqlc.types.Field(String, graphql_name='enterpriseSlug')
    enterprise_url = sgqlc.types.Field(URI, graphql_name='enterpriseUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgOauthAppAccessApprovedAuditEntry(sgqlc.types.Type, Node, AuditEntry, OauthApplicationAuditEntryData, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    oauth_application_name = sgqlc.types.Field(String, graphql_name='oauthApplicationName')
    oauth_application_resource_path = sgqlc.types.Field(URI, graphql_name='oauthApplicationResourcePath')
    oauth_application_url = sgqlc.types.Field(URI, graphql_name='oauthApplicationUrl')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgOauthAppAccessDeniedAuditEntry(sgqlc.types.Type, Node, AuditEntry, OauthApplicationAuditEntryData, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    oauth_application_name = sgqlc.types.Field(String, graphql_name='oauthApplicationName')
    oauth_application_resource_path = sgqlc.types.Field(URI, graphql_name='oauthApplicationResourcePath')
    oauth_application_url = sgqlc.types.Field(URI, graphql_name='oauthApplicationUrl')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgOauthAppAccessRequestedAuditEntry(sgqlc.types.Type, Node, AuditEntry, OauthApplicationAuditEntryData, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    oauth_application_name = sgqlc.types.Field(String, graphql_name='oauthApplicationName')
    oauth_application_resource_path = sgqlc.types.Field(URI, graphql_name='oauthApplicationResourcePath')
    oauth_application_url = sgqlc.types.Field(URI, graphql_name='oauthApplicationUrl')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgRemoveBillingManagerAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    reason = sgqlc.types.Field(OrgRemoveBillingManagerAuditEntryReason, graphql_name='reason')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgRemoveMemberAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    membership_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(OrgRemoveMemberAuditEntryMembershipType)), graphql_name='membershipTypes')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    reason = sgqlc.types.Field(OrgRemoveMemberAuditEntryReason, graphql_name='reason')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgRemoveOutsideCollaboratorAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    membership_types = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(OrgRemoveOutsideCollaboratorAuditEntryMembershipType)), graphql_name='membershipTypes')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    reason = sgqlc.types.Field(OrgRemoveOutsideCollaboratorAuditEntryReason, graphql_name='reason')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgRestoreMemberAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    restored_custom_email_routings_count = sgqlc.types.Field(Int, graphql_name='restoredCustomEmailRoutingsCount')
    restored_issue_assignments_count = sgqlc.types.Field(Int, graphql_name='restoredIssueAssignmentsCount')
    restored_memberships = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('OrgRestoreMemberAuditEntryMembership')), graphql_name='restoredMemberships')
    restored_memberships_count = sgqlc.types.Field(Int, graphql_name='restoredMembershipsCount')
    restored_repositories_count = sgqlc.types.Field(Int, graphql_name='restoredRepositoriesCount')
    restored_repository_stars_count = sgqlc.types.Field(Int, graphql_name='restoredRepositoryStarsCount')
    restored_repository_watches_count = sgqlc.types.Field(Int, graphql_name='restoredRepositoryWatchesCount')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgRestoreMemberMembershipOrganizationAuditEntryData(sgqlc.types.Type, OrganizationAuditEntryData):
    __schema__ = github_schema
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')


class OrgRestoreMemberMembershipRepositoryAuditEntryData(sgqlc.types.Type, RepositoryAuditEntryData):
    __schema__ = github_schema
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')


class OrgRestoreMemberMembershipTeamAuditEntryData(sgqlc.types.Type, TeamAuditEntryData):
    __schema__ = github_schema
    team = sgqlc.types.Field('Team', graphql_name='team')
    team_name = sgqlc.types.Field(String, graphql_name='teamName')
    team_resource_path = sgqlc.types.Field(URI, graphql_name='teamResourcePath')
    team_url = sgqlc.types.Field(URI, graphql_name='teamUrl')


class OrgUnblockUserAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    blocked_user = sgqlc.types.Field('User', graphql_name='blockedUser')
    blocked_user_name = sgqlc.types.Field(String, graphql_name='blockedUserName')
    blocked_user_resource_path = sgqlc.types.Field(URI, graphql_name='blockedUserResourcePath')
    blocked_user_url = sgqlc.types.Field(URI, graphql_name='blockedUserUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgUpdateDefaultRepositoryPermissionAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    permission = sgqlc.types.Field(OrgUpdateDefaultRepositoryPermissionAuditEntryPermission, graphql_name='permission')
    permission_was = sgqlc.types.Field(OrgUpdateDefaultRepositoryPermissionAuditEntryPermission, graphql_name='permissionWas')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgUpdateMemberAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    permission = sgqlc.types.Field(OrgUpdateMemberAuditEntryPermission, graphql_name='permission')
    permission_was = sgqlc.types.Field(OrgUpdateMemberAuditEntryPermission, graphql_name='permissionWas')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class OrgUpdateMemberRepositoryCreationPermissionAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    can_create_repositories = sgqlc.types.Field(Boolean, graphql_name='canCreateRepositories')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')
    visibility = sgqlc.types.Field(OrgUpdateMemberRepositoryCreationPermissionAuditEntryVisibility, graphql_name='visibility')


class OrgUpdateMemberRepositoryInvitationPermissionAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    can_invite_outside_collaborators_to_repositories = sgqlc.types.Field(Boolean, graphql_name='canInviteOutsideCollaboratorsToRepositories')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field('Organization', graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class Organization(sgqlc.types.Type, Node, Actor, RegistryPackageOwner, RegistryPackageSearch, ProjectOwner, RepositoryOwner, UniformResourceLocatable, MemberStatusable, ProfileOwner, Sponsorable):
    __schema__ = github_schema
    any_pinnable_items = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='anyPinnableItems', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(PinnableItemType, graphql_name='type', default=None)),
))
    )
    audit_log = sgqlc.types.Field(sgqlc.types.non_null(OrganizationAuditEntryConnection), graphql_name='auditLog', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(AuditLogOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'DESC'})),
))
    )
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_html = sgqlc.types.Field(String, graphql_name='descriptionHTML')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_verified = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVerified')
    item_showcase = sgqlc.types.Field(sgqlc.types.non_null(ProfileItemShowcase), graphql_name='itemShowcase')
    location = sgqlc.types.Field(String, graphql_name='location')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    member_statuses = sgqlc.types.Field(sgqlc.types.non_null(UserStatusConnection), graphql_name='memberStatuses', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(UserStatusOrder, graphql_name='orderBy', default={'field': 'UPDATED_AT', 'direction': 'DESC'})),
))
    )
    members_with_role = sgqlc.types.Field(sgqlc.types.non_null(OrganizationMemberConnection), graphql_name='membersWithRole', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    name = sgqlc.types.Field(String, graphql_name='name')
    new_team_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='newTeamResourcePath')
    new_team_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='newTeamUrl')
    organization_billing_email = sgqlc.types.Field(String, graphql_name='organizationBillingEmail')
    pending_members = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='pendingMembers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pinnable_items = sgqlc.types.Field(sgqlc.types.non_null(PinnableItemConnection), graphql_name='pinnableItems', args=sgqlc.types.ArgDict((
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PinnableItemType)), graphql_name='types', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pinned_items = sgqlc.types.Field(sgqlc.types.non_null(PinnableItemConnection), graphql_name='pinnedItems', args=sgqlc.types.ArgDict((
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PinnableItemType)), graphql_name='types', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pinned_items_remaining = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pinnedItemsRemaining')
    project = sgqlc.types.Field('Project', graphql_name='project', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    projects = sgqlc.types.Field(sgqlc.types.non_null(ProjectConnection), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(ProjectOrder, graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectState)), graphql_name='states', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    projects_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsResourcePath')
    projects_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsUrl')
    repositories = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=['OWNER', 'COLLABORATOR'])),
        ('owner_affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='ownerAffiliations', default=['OWNER', 'COLLABORATOR'])),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('is_fork', sgqlc.types.Arg(Boolean, graphql_name='isFork', default=None)),
))
    )
    repository = sgqlc.types.Field('Repository', graphql_name='repository', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    requires_two_factor_authentication = sgqlc.types.Field(Boolean, graphql_name='requiresTwoFactorAuthentication')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    saml_identity_provider = sgqlc.types.Field('OrganizationIdentityProvider', graphql_name='samlIdentityProvider')
    sponsors_listing = sgqlc.types.Field('SponsorsListing', graphql_name='sponsorsListing')
    sponsorships_as_maintainer = sgqlc.types.Field(sgqlc.types.non_null(SponsorshipConnection), graphql_name='sponsorshipsAsMaintainer', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_private', sgqlc.types.Arg(Boolean, graphql_name='includePrivate', default=False)),
        ('order_by', sgqlc.types.Arg(SponsorshipOrder, graphql_name='orderBy', default=None)),
))
    )
    sponsorships_as_sponsor = sgqlc.types.Field(sgqlc.types.non_null(SponsorshipConnection), graphql_name='sponsorshipsAsSponsor', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(SponsorshipOrder, graphql_name='orderBy', default=None)),
))
    )
    team = sgqlc.types.Field('Team', graphql_name='team', args=sgqlc.types.ArgDict((
        ('slug', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='slug', default=None)),
))
    )
    teams = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='teams', args=sgqlc.types.ArgDict((
        ('privacy', sgqlc.types.Arg(TeamPrivacy, graphql_name='privacy', default=None)),
        ('role', sgqlc.types.Arg(TeamRole, graphql_name='role', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('user_logins', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='userLogins', default=None)),
        ('order_by', sgqlc.types.Arg(TeamOrder, graphql_name='orderBy', default=None)),
        ('ldap_mapped', sgqlc.types.Arg(Boolean, graphql_name='ldapMapped', default=None)),
        ('root_teams_only', sgqlc.types.Arg(Boolean, graphql_name='rootTeamsOnly', default=False)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    teams_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsResourcePath')
    teams_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsUrl')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_administer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanAdminister')
    viewer_can_change_pinned_items = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanChangePinnedItems')
    viewer_can_create_projects = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanCreateProjects')
    viewer_can_create_repositories = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanCreateRepositories')
    viewer_can_create_teams = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanCreateTeams')
    viewer_is_amember = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerIsAMember')
    website_url = sgqlc.types.Field(URI, graphql_name='websiteUrl')


class OrganizationIdentityProvider(sgqlc.types.Type, Node):
    __schema__ = github_schema
    digest_method = sgqlc.types.Field(URI, graphql_name='digestMethod')
    external_identities = sgqlc.types.Field(sgqlc.types.non_null(ExternalIdentityConnection), graphql_name='externalIdentities', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    idp_certificate = sgqlc.types.Field(X509Certificate, graphql_name='idpCertificate')
    issuer = sgqlc.types.Field(String, graphql_name='issuer')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    signature_method = sgqlc.types.Field(URI, graphql_name='signatureMethod')
    sso_url = sgqlc.types.Field(URI, graphql_name='ssoUrl')


class OrganizationInvitation(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    email = sgqlc.types.Field(String, graphql_name='email')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    invitation_type = sgqlc.types.Field(sgqlc.types.non_null(OrganizationInvitationType), graphql_name='invitationType')
    invitee = sgqlc.types.Field('User', graphql_name='invitee')
    inviter = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='inviter')
    organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='organization')
    role = sgqlc.types.Field(sgqlc.types.non_null(OrganizationInvitationRole), graphql_name='role')


class OrganizationTeamsHovercardContext(sgqlc.types.Type, HovercardContext):
    __schema__ = github_schema
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    octicon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='octicon')
    relevant_teams = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='relevantTeams', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    teams_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsResourcePath')
    teams_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsUrl')
    total_team_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalTeamCount')


class OrganizationsHovercardContext(sgqlc.types.Type, HovercardContext):
    __schema__ = github_schema
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    octicon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='octicon')
    relevant_organizations = sgqlc.types.Field(sgqlc.types.non_null(OrganizationConnection), graphql_name='relevantOrganizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    total_organization_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalOrganizationCount')


class PinnedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')


class PrivateRepositoryForkingDisableAuditEntry(sgqlc.types.Type, Node, AuditEntry, EnterpriseAuditEntryData, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    enterprise_resource_path = sgqlc.types.Field(URI, graphql_name='enterpriseResourcePath')
    enterprise_slug = sgqlc.types.Field(String, graphql_name='enterpriseSlug')
    enterprise_url = sgqlc.types.Field(URI, graphql_name='enterpriseUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class PrivateRepositoryForkingEnableAuditEntry(sgqlc.types.Type, Node, AuditEntry, EnterpriseAuditEntryData, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    enterprise_resource_path = sgqlc.types.Field(URI, graphql_name='enterpriseResourcePath')
    enterprise_slug = sgqlc.types.Field(String, graphql_name='enterpriseSlug')
    enterprise_url = sgqlc.types.Field(URI, graphql_name='enterpriseUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class Project(sgqlc.types.Type, Node, Closable, Updatable):
    __schema__ = github_schema
    body = sgqlc.types.Field(String, graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    closed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='closed')
    closed_at = sgqlc.types.Field(DateTime, graphql_name='closedAt')
    columns = sgqlc.types.Field(sgqlc.types.non_null(ProjectColumnConnection), graphql_name='columns', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    owner = sgqlc.types.Field(sgqlc.types.non_null(ProjectOwner), graphql_name='owner')
    pending_cards = sgqlc.types.Field(sgqlc.types.non_null(ProjectCardConnection), graphql_name='pendingCards', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('archived_states', sgqlc.types.Arg(sgqlc.types.list_of(ProjectCardArchivedState), graphql_name='archivedStates', default=['ARCHIVED', 'NOT_ARCHIVED'])),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    state = sgqlc.types.Field(sgqlc.types.non_null(ProjectState), graphql_name='state')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')


class ProjectCard(sgqlc.types.Type, Node):
    __schema__ = github_schema
    column = sgqlc.types.Field('ProjectColumn', graphql_name='column')
    content = sgqlc.types.Field('ProjectCardItem', graphql_name='content')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_archived = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isArchived')
    note = sgqlc.types.Field(String, graphql_name='note')
    project = sgqlc.types.Field(sgqlc.types.non_null(Project), graphql_name='project')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    state = sgqlc.types.Field(ProjectCardState, graphql_name='state')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class ProjectColumn(sgqlc.types.Type, Node):
    __schema__ = github_schema
    cards = sgqlc.types.Field(sgqlc.types.non_null(ProjectCardConnection), graphql_name='cards', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('archived_states', sgqlc.types.Arg(sgqlc.types.list_of(ProjectCardArchivedState), graphql_name='archivedStates', default=['ARCHIVED', 'NOT_ARCHIVED'])),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    project = sgqlc.types.Field(sgqlc.types.non_null(Project), graphql_name='project')
    purpose = sgqlc.types.Field(ProjectColumnPurpose, graphql_name='purpose')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class PublicKey(sgqlc.types.Type, Node):
    __schema__ = github_schema
    accessed_at = sgqlc.types.Field(DateTime, graphql_name='accessedAt')
    created_at = sgqlc.types.Field(DateTime, graphql_name='createdAt')
    fingerprint = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fingerprint')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_read_only = sgqlc.types.Field(Boolean, graphql_name='isReadOnly')
    key = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='key')
    updated_at = sgqlc.types.Field(DateTime, graphql_name='updatedAt')


class PullRequest(sgqlc.types.Type, Node, Assignable, Closable, Comment, Updatable, UpdatableComment, Labelable, Lockable, Reactable, RepositoryNode, Subscribable, UniformResourceLocatable):
    __schema__ = github_schema
    active_lock_reason = sgqlc.types.Field(LockReason, graphql_name='activeLockReason')
    additions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='additions')
    assignees = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='assignees', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    base_ref = sgqlc.types.Field('Ref', graphql_name='baseRef')
    base_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='baseRefName')
    base_ref_oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='baseRefOid')
    base_repository = sgqlc.types.Field('Repository', graphql_name='baseRepository')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    changed_files = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='changedFiles')
    closed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='closed')
    closed_at = sgqlc.types.Field(DateTime, graphql_name='closedAt')
    comments = sgqlc.types.Field(sgqlc.types.non_null(IssueCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    commits = sgqlc.types.Field(sgqlc.types.non_null(PullRequestCommitConnection), graphql_name='commits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    deletions = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='deletions')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    files = sgqlc.types.Field(PullRequestChangedFileConnection, graphql_name='files', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    head_ref = sgqlc.types.Field('Ref', graphql_name='headRef')
    head_ref_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='headRefName')
    head_ref_oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='headRefOid')
    head_repository = sgqlc.types.Field('Repository', graphql_name='headRepository')
    head_repository_owner = sgqlc.types.Field(RepositoryOwner, graphql_name='headRepositoryOwner')
    hovercard = sgqlc.types.Field(sgqlc.types.non_null(Hovercard), graphql_name='hovercard', args=sgqlc.types.ArgDict((
        ('include_notification_contexts', sgqlc.types.Arg(Boolean, graphql_name='includeNotificationContexts', default=True)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    includes_created_edit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includesCreatedEdit')
    is_cross_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCrossRepository')
    labels = sgqlc.types.Field(LabelConnection, graphql_name='labels', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    locked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='locked')
    maintainer_can_modify = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='maintainerCanModify')
    merge_commit = sgqlc.types.Field(Commit, graphql_name='mergeCommit')
    mergeable = sgqlc.types.Field(sgqlc.types.non_null(MergeableState), graphql_name='mergeable')
    merged = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='merged')
    merged_at = sgqlc.types.Field(DateTime, graphql_name='mergedAt')
    merged_by = sgqlc.types.Field(Actor, graphql_name='mergedBy')
    milestone = sgqlc.types.Field(Milestone, graphql_name='milestone')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    participants = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='participants', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    permalink = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='permalink')
    potential_merge_commit = sgqlc.types.Field(Commit, graphql_name='potentialMergeCommit')
    project_cards = sgqlc.types.Field(sgqlc.types.non_null(ProjectCardConnection), graphql_name='projectCards', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('archived_states', sgqlc.types.Arg(sgqlc.types.list_of(ProjectCardArchivedState), graphql_name='archivedStates', default=['ARCHIVED', 'NOT_ARCHIVED'])),
))
    )
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ReactionGroup)), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(ReactionConnection), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    revert_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='revertResourcePath')
    revert_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='revertUrl')
    review_requests = sgqlc.types.Field(ReviewRequestConnection, graphql_name='reviewRequests', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    review_threads = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewThreadConnection), graphql_name='reviewThreads', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    reviews = sgqlc.types.Field(PullRequestReviewConnection, graphql_name='reviews', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestReviewState)), graphql_name='states', default=None)),
        ('author', sgqlc.types.Arg(String, graphql_name='author', default=None)),
))
    )
    state = sgqlc.types.Field(sgqlc.types.non_null(PullRequestState), graphql_name='state')
    suggested_reviewers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(SuggestedReviewer)), graphql_name='suggestedReviewers')
    timeline_items = sgqlc.types.Field(sgqlc.types.non_null(PullRequestTimelineItemsConnection), graphql_name='timelineItems', args=sgqlc.types.ArgDict((
        ('since', sgqlc.types.Arg(DateTime, graphql_name='since', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('item_types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestTimelineItemsItemType)), graphql_name='itemTypes', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    viewer_can_apply_suggestion = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanApplySuggestion')
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')
    viewer_can_subscribe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSubscribe')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')
    viewer_subscription = sgqlc.types.Field(SubscriptionState, graphql_name='viewerSubscription')


class PullRequestCommit(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = github_schema
    commit = sgqlc.types.Field(sgqlc.types.non_null(Commit), graphql_name='commit')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class PullRequestCommitCommentThread(sgqlc.types.Type, Node, RepositoryNode):
    __schema__ = github_schema
    comments = sgqlc.types.Field(sgqlc.types.non_null(CommitCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    commit = sgqlc.types.Field(sgqlc.types.non_null(Commit), graphql_name='commit')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    path = sgqlc.types.Field(String, graphql_name='path')
    position = sgqlc.types.Field(Int, graphql_name='position')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')


class PullRequestReview(sgqlc.types.Type, Node, Comment, Deletable, Updatable, UpdatableComment, Reactable, RepositoryNode):
    __schema__ = github_schema
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    comments = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    includes_created_edit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includesCreatedEdit')
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    on_behalf_of = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='onBehalfOf', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ReactionGroup)), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(ReactionConnection), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    state = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewState), graphql_name='state')
    submitted_at = sgqlc.types.Field(DateTime, graphql_name='submittedAt')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    viewer_can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelete')
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')


class PullRequestReviewComment(sgqlc.types.Type, Node, Comment, Deletable, Updatable, UpdatableComment, Reactable, RepositoryNode):
    __schema__ = github_schema
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    diff_hunk = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='diffHunk')
    drafted_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='draftedAt')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    includes_created_edit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includesCreatedEdit')
    is_minimized = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMinimized')
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    minimized_reason = sgqlc.types.Field(String, graphql_name='minimizedReason')
    original_commit = sgqlc.types.Field(Commit, graphql_name='originalCommit')
    original_position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='originalPosition')
    outdated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='outdated')
    path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='path')
    position = sgqlc.types.Field(Int, graphql_name='position')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    pull_request_review = sgqlc.types.Field(PullRequestReview, graphql_name='pullRequestReview')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ReactionGroup)), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(ReactionConnection), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    reply_to = sgqlc.types.Field('PullRequestReviewComment', graphql_name='replyTo')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    state = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewCommentState), graphql_name='state')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    viewer_can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelete')
    viewer_can_minimize = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanMinimize')
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')


class PullRequestReviewThread(sgqlc.types.Type, Node):
    __schema__ = github_schema
    comments = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_resolved = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isResolved')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    resolved_by = sgqlc.types.Field('User', graphql_name='resolvedBy')
    viewer_can_resolve = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanResolve')
    viewer_can_unresolve = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUnresolve')


class PushAllowance(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field('PushAllowanceActor', graphql_name='actor')
    branch_protection_rule = sgqlc.types.Field(BranchProtectionRule, graphql_name='branchProtectionRule')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class Reaction(sgqlc.types.Type, Node):
    __schema__ = github_schema
    content = sgqlc.types.Field(sgqlc.types.non_null(ReactionContent), graphql_name='content')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    reactable = sgqlc.types.Field(sgqlc.types.non_null(Reactable), graphql_name='reactable')
    user = sgqlc.types.Field('User', graphql_name='user')


class ReadyForReviewEvent(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class Ref(sgqlc.types.Type, Node):
    __schema__ = github_schema
    associated_pull_requests = sgqlc.types.Field(sgqlc.types.non_null(PullRequestConnection), graphql_name='associatedPullRequests', args=sgqlc.types.ArgDict((
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    prefix = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='prefix')
    repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='repository')
    target = sgqlc.types.Field(sgqlc.types.non_null(GitObject), graphql_name='target')


class ReferencedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    commit_repository = sgqlc.types.Field(sgqlc.types.non_null('Repository'), graphql_name='commitRepository')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_cross_repository = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCrossRepository')
    is_direct_reference = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDirectReference')
    subject = sgqlc.types.Field(sgqlc.types.non_null('ReferencedSubject'), graphql_name='subject')


class RegistryPackage(sgqlc.types.Type, Node):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class RegistryPackageDependency(sgqlc.types.Type, Node):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class RegistryPackageFile(sgqlc.types.Type, Node):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class RegistryPackageTag(sgqlc.types.Type, Node):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class RegistryPackageVersion(sgqlc.types.Type, Node):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class Release(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = github_schema
    author = sgqlc.types.Field('User', graphql_name='author')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    description_html = sgqlc.types.Field(HTML, graphql_name='descriptionHTML')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_draft = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDraft')
    is_prerelease = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrerelease')
    name = sgqlc.types.Field(String, graphql_name='name')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    release_assets = sgqlc.types.Field(sgqlc.types.non_null(ReleaseAssetConnection), graphql_name='releaseAssets', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('name', sgqlc.types.Arg(String, graphql_name='name', default=None)),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    short_description_html = sgqlc.types.Field(HTML, graphql_name='shortDescriptionHTML', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=200)),
))
    )
    tag = sgqlc.types.Field(Ref, graphql_name='tag')
    tag_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tagName')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class ReleaseAsset(sgqlc.types.Type, Node):
    __schema__ = github_schema
    content_type = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contentType')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    download_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='downloadCount')
    download_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='downloadUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    release = sgqlc.types.Field(Release, graphql_name='release')
    size = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='size')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    uploaded_by = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='uploadedBy')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class RemovedFromProjectEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class RenamedTitleEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    current_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='currentTitle')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    previous_title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='previousTitle')
    subject = sgqlc.types.Field(sgqlc.types.non_null('RenamedTitleSubject'), graphql_name='subject')


class ReopenedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    closable = sgqlc.types.Field(sgqlc.types.non_null(Closable), graphql_name='closable')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class RepoAccessAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')
    visibility = sgqlc.types.Field(RepoAccessAuditEntryVisibility, graphql_name='visibility')


class RepoAddMemberAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')
    visibility = sgqlc.types.Field(RepoAddMemberAuditEntryVisibility, graphql_name='visibility')


class RepoAddTopicAuditEntry(sgqlc.types.Type, Node, AuditEntry, RepositoryAuditEntryData, OrganizationAuditEntryData, TopicAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    topic = sgqlc.types.Field('Topic', graphql_name='topic')
    topic_name = sgqlc.types.Field(String, graphql_name='topicName')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class RepoArchivedAuditEntry(sgqlc.types.Type, Node, AuditEntry, RepositoryAuditEntryData, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')
    visibility = sgqlc.types.Field(RepoArchivedAuditEntryVisibility, graphql_name='visibility')


class RepoChangeMergeSettingAuditEntry(sgqlc.types.Type, Node, AuditEntry, RepositoryAuditEntryData, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_enabled = sgqlc.types.Field(Boolean, graphql_name='isEnabled')
    merge_type = sgqlc.types.Field(RepoChangeMergeSettingAuditEntryMergeType, graphql_name='mergeType')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class RepoConfigDisableAnonymousGitAccessAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class RepoConfigDisableCollaboratorsOnlyAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class RepoConfigDisableContributorsOnlyAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class RepoConfigDisableSockpuppetDisallowedAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class RepoConfigEnableAnonymousGitAccessAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class RepoConfigEnableCollaboratorsOnlyAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class RepoConfigEnableContributorsOnlyAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class RepoConfigEnableSockpuppetDisallowedAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class RepoConfigLockAnonymousGitAccessAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class RepoConfigUnlockAnonymousGitAccessAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class RepoCreateAuditEntry(sgqlc.types.Type, Node, AuditEntry, RepositoryAuditEntryData, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    fork_parent_name = sgqlc.types.Field(String, graphql_name='forkParentName')
    fork_source_name = sgqlc.types.Field(String, graphql_name='forkSourceName')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')
    visibility = sgqlc.types.Field(RepoCreateAuditEntryVisibility, graphql_name='visibility')


class RepoDestroyAuditEntry(sgqlc.types.Type, Node, AuditEntry, RepositoryAuditEntryData, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')
    visibility = sgqlc.types.Field(RepoDestroyAuditEntryVisibility, graphql_name='visibility')


class RepoRemoveMemberAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, RepositoryAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')
    visibility = sgqlc.types.Field(RepoRemoveMemberAuditEntryVisibility, graphql_name='visibility')


class RepoRemoveTopicAuditEntry(sgqlc.types.Type, Node, AuditEntry, RepositoryAuditEntryData, OrganizationAuditEntryData, TopicAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field('Repository', graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    topic = sgqlc.types.Field('Topic', graphql_name='topic')
    topic_name = sgqlc.types.Field(String, graphql_name='topicName')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class Repository(sgqlc.types.Type, Node, ProjectOwner, RegistryPackageOwner, RegistryPackageSearch, Subscribable, Starrable, UniformResourceLocatable, RepositoryInfo):
    __schema__ = github_schema
    assignable_users = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='assignableUsers', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    branch_protection_rules = sgqlc.types.Field(sgqlc.types.non_null(BranchProtectionRuleConnection), graphql_name='branchProtectionRules', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    code_of_conduct = sgqlc.types.Field(CodeOfConduct, graphql_name='codeOfConduct')
    collaborators = sgqlc.types.Field(RepositoryCollaboratorConnection, graphql_name='collaborators', args=sgqlc.types.ArgDict((
        ('affiliation', sgqlc.types.Arg(CollaboratorAffiliation, graphql_name='affiliation', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    commit_comments = sgqlc.types.Field(sgqlc.types.non_null(CommitCommentConnection), graphql_name='commitComments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    default_branch_ref = sgqlc.types.Field(Ref, graphql_name='defaultBranchRef')
    deploy_keys = sgqlc.types.Field(sgqlc.types.non_null(DeployKeyConnection), graphql_name='deployKeys', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    deployments = sgqlc.types.Field(sgqlc.types.non_null(DeploymentConnection), graphql_name='deployments', args=sgqlc.types.ArgDict((
        ('environments', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='environments', default=None)),
        ('order_by', sgqlc.types.Arg(DeploymentOrder, graphql_name='orderBy', default={'field': 'CREATED_AT', 'direction': 'ASC'})),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    description = sgqlc.types.Field(String, graphql_name='description')
    description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='descriptionHTML')
    disk_usage = sgqlc.types.Field(Int, graphql_name='diskUsage')
    fork_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='forkCount')
    forks = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='forks', args=sgqlc.types.ArgDict((
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=['OWNER', 'COLLABORATOR'])),
        ('owner_affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='ownerAffiliations', default=['OWNER', 'COLLABORATOR'])),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    funding_links = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(FundingLink))), graphql_name='fundingLinks')
    has_issues_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasIssuesEnabled')
    has_projects_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasProjectsEnabled')
    has_wiki_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasWikiEnabled')
    homepage_url = sgqlc.types.Field(URI, graphql_name='homepageUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_archived = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isArchived')
    is_disabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDisabled')
    is_fork = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isFork')
    is_locked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLocked')
    is_mirror = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isMirror')
    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    is_template = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTemplate')
    issue = sgqlc.types.Field(Issue, graphql_name='issue', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    issue_or_pull_request = sgqlc.types.Field('IssueOrPullRequest', graphql_name='issueOrPullRequest', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='states', default=None)),
        ('filter_by', sgqlc.types.Arg(IssueFilters, graphql_name='filterBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    label = sgqlc.types.Field(Label, graphql_name='label', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    labels = sgqlc.types.Field(LabelConnection, graphql_name='labels', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
))
    )
    languages = sgqlc.types.Field(LanguageConnection, graphql_name='languages', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(LanguageOrder, graphql_name='orderBy', default=None)),
))
    )
    license_info = sgqlc.types.Field(License, graphql_name='licenseInfo')
    lock_reason = sgqlc.types.Field(RepositoryLockReason, graphql_name='lockReason')
    mentionable_users = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='mentionableUsers', args=sgqlc.types.ArgDict((
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    merge_commit_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='mergeCommitAllowed')
    milestone = sgqlc.types.Field(Milestone, graphql_name='milestone', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    milestones = sgqlc.types.Field(MilestoneConnection, graphql_name='milestones', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(MilestoneState)), graphql_name='states', default=None)),
        ('order_by', sgqlc.types.Arg(MilestoneOrder, graphql_name='orderBy', default=None)),
))
    )
    mirror_url = sgqlc.types.Field(URI, graphql_name='mirrorUrl')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    name_with_owner = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='nameWithOwner')
    object = sgqlc.types.Field(GitObject, graphql_name='object', args=sgqlc.types.ArgDict((
        ('oid', sgqlc.types.Arg(GitObjectID, graphql_name='oid', default=None)),
        ('expression', sgqlc.types.Arg(String, graphql_name='expression', default=None)),
))
    )
    open_graph_image_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='openGraphImageUrl')
    owner = sgqlc.types.Field(sgqlc.types.non_null(RepositoryOwner), graphql_name='owner')
    parent = sgqlc.types.Field('Repository', graphql_name='parent')
    primary_language = sgqlc.types.Field(Language, graphql_name='primaryLanguage')
    project = sgqlc.types.Field(Project, graphql_name='project', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    projects = sgqlc.types.Field(sgqlc.types.non_null(ProjectConnection), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(ProjectOrder, graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectState)), graphql_name='states', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    projects_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsResourcePath')
    projects_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsUrl')
    pull_request = sgqlc.types.Field(PullRequest, graphql_name='pullRequest', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    pull_requests = sgqlc.types.Field(sgqlc.types.non_null(PullRequestConnection), graphql_name='pullRequests', args=sgqlc.types.ArgDict((
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pushed_at = sgqlc.types.Field(DateTime, graphql_name='pushedAt')
    rebase_merge_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='rebaseMergeAllowed')
    ref = sgqlc.types.Field(Ref, graphql_name='ref', args=sgqlc.types.ArgDict((
        ('qualified_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='qualifiedName', default=None)),
))
    )
    refs = sgqlc.types.Field(RefConnection, graphql_name='refs', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('ref_prefix', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='refPrefix', default=None)),
        ('direction', sgqlc.types.Arg(OrderDirection, graphql_name='direction', default=None)),
        ('order_by', sgqlc.types.Arg(RefOrder, graphql_name='orderBy', default=None)),
))
    )
    release = sgqlc.types.Field(Release, graphql_name='release', args=sgqlc.types.ArgDict((
        ('tag_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tagName', default=None)),
))
    )
    releases = sgqlc.types.Field(sgqlc.types.non_null(ReleaseConnection), graphql_name='releases', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(ReleaseOrder, graphql_name='orderBy', default=None)),
))
    )
    repository_topics = sgqlc.types.Field(sgqlc.types.non_null(RepositoryTopicConnection), graphql_name='repositoryTopics', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    short_description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='shortDescriptionHTML', args=sgqlc.types.ArgDict((
        ('limit', sgqlc.types.Arg(Int, graphql_name='limit', default=200)),
))
    )
    squash_merge_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='squashMergeAllowed')
    ssh_url = sgqlc.types.Field(sgqlc.types.non_null(GitSSHRemote), graphql_name='sshUrl')
    stargazers = sgqlc.types.Field(sgqlc.types.non_null(StargazerConnection), graphql_name='stargazers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(StarOrder, graphql_name='orderBy', default=None)),
))
    )
    template_repository = sgqlc.types.Field('Repository', graphql_name='templateRepository')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    uses_custom_open_graph_image = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='usesCustomOpenGraphImage')
    viewer_can_administer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanAdminister')
    viewer_can_create_projects = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanCreateProjects')
    viewer_can_subscribe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSubscribe')
    viewer_can_update_topics = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdateTopics')
    viewer_has_starred = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasStarred')
    viewer_permission = sgqlc.types.Field(RepositoryPermission, graphql_name='viewerPermission')
    viewer_subscription = sgqlc.types.Field(SubscriptionState, graphql_name='viewerSubscription')
    vulnerability_alerts = sgqlc.types.Field(RepositoryVulnerabilityAlertConnection, graphql_name='vulnerabilityAlerts', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    watchers = sgqlc.types.Field(sgqlc.types.non_null(UserConnection), graphql_name='watchers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )


class RepositoryInvitation(sgqlc.types.Type, Node):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    invitee = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='invitee')
    inviter = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='inviter')
    permission = sgqlc.types.Field(sgqlc.types.non_null(RepositoryPermission), graphql_name='permission')
    repository = sgqlc.types.Field(RepositoryInfo, graphql_name='repository')


class RepositoryTopic(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    topic = sgqlc.types.Field(sgqlc.types.non_null('Topic'), graphql_name='topic')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class RepositoryVisibilityChangeDisableAuditEntry(sgqlc.types.Type, Node, AuditEntry, EnterpriseAuditEntryData, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    enterprise_resource_path = sgqlc.types.Field(URI, graphql_name='enterpriseResourcePath')
    enterprise_slug = sgqlc.types.Field(String, graphql_name='enterpriseSlug')
    enterprise_url = sgqlc.types.Field(URI, graphql_name='enterpriseUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class RepositoryVisibilityChangeEnableAuditEntry(sgqlc.types.Type, Node, AuditEntry, EnterpriseAuditEntryData, OrganizationAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    enterprise_resource_path = sgqlc.types.Field(URI, graphql_name='enterpriseResourcePath')
    enterprise_slug = sgqlc.types.Field(String, graphql_name='enterpriseSlug')
    enterprise_url = sgqlc.types.Field(URI, graphql_name='enterpriseUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class RepositoryVulnerabilityAlert(sgqlc.types.Type, Node, RepositoryNode):
    __schema__ = github_schema
    dismiss_reason = sgqlc.types.Field(String, graphql_name='dismissReason')
    dismissed_at = sgqlc.types.Field(DateTime, graphql_name='dismissedAt')
    dismisser = sgqlc.types.Field('User', graphql_name='dismisser')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    security_advisory = sgqlc.types.Field('SecurityAdvisory', graphql_name='securityAdvisory')
    security_vulnerability = sgqlc.types.Field(SecurityVulnerability, graphql_name='securityVulnerability')
    vulnerable_manifest_filename = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vulnerableManifestFilename')
    vulnerable_manifest_path = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='vulnerableManifestPath')
    vulnerable_requirements = sgqlc.types.Field(String, graphql_name='vulnerableRequirements')


class RestrictedContribution(sgqlc.types.Type, Contribution):
    __schema__ = github_schema
    is_restricted = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRestricted')
    occurred_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='occurredAt')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='user')


class ReviewDismissalAllowance(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field('ReviewDismissalAllowanceActor', graphql_name='actor')
    branch_protection_rule = sgqlc.types.Field(BranchProtectionRule, graphql_name='branchProtectionRule')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class ReviewDismissedEvent(sgqlc.types.Type, Node, UniformResourceLocatable):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    dismissal_message = sgqlc.types.Field(String, graphql_name='dismissalMessage')
    dismissal_message_html = sgqlc.types.Field(String, graphql_name='dismissalMessageHTML')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    previous_review_state = sgqlc.types.Field(sgqlc.types.non_null(PullRequestReviewState), graphql_name='previousReviewState')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    pull_request_commit = sgqlc.types.Field(PullRequestCommit, graphql_name='pullRequestCommit')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    review = sgqlc.types.Field(PullRequestReview, graphql_name='review')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')


class ReviewRequest(sgqlc.types.Type, Node):
    __schema__ = github_schema
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    requested_reviewer = sgqlc.types.Field('RequestedReviewer', graphql_name='requestedReviewer')


class ReviewRequestRemovedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    requested_reviewer = sgqlc.types.Field('RequestedReviewer', graphql_name='requestedReviewer')


class ReviewRequestedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    pull_request = sgqlc.types.Field(sgqlc.types.non_null(PullRequest), graphql_name='pullRequest')
    requested_reviewer = sgqlc.types.Field('RequestedReviewer', graphql_name='requestedReviewer')


class ReviewStatusHovercardContext(sgqlc.types.Type, HovercardContext):
    __schema__ = github_schema
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    octicon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='octicon')


class SavedReply(sgqlc.types.Type, Node):
    __schema__ = github_schema
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    user = sgqlc.types.Field(Actor, graphql_name='user')


class SecurityAdvisory(sgqlc.types.Type, Node):
    __schema__ = github_schema
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    ghsa_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ghsaId')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    identifiers = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SecurityAdvisoryIdentifier))), graphql_name='identifiers')
    origin = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='origin')
    published_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='publishedAt')
    references = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(SecurityAdvisoryReference))), graphql_name='references')
    severity = sgqlc.types.Field(sgqlc.types.non_null(SecurityAdvisorySeverity), graphql_name='severity')
    summary = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='summary')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    vulnerabilities = sgqlc.types.Field(sgqlc.types.non_null(SecurityVulnerabilityConnection), graphql_name='vulnerabilities', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(SecurityVulnerabilityOrder, graphql_name='orderBy', default={'field': 'UPDATED_AT', 'direction': 'DESC'})),
        ('ecosystem', sgqlc.types.Arg(SecurityAdvisoryEcosystem, graphql_name='ecosystem', default=None)),
        ('package', sgqlc.types.Arg(String, graphql_name='package', default=None)),
        ('severities', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SecurityAdvisorySeverity)), graphql_name='severities', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    withdrawn_at = sgqlc.types.Field(DateTime, graphql_name='withdrawnAt')


class SmimeSignature(sgqlc.types.Type, GitSignature):
    __schema__ = github_schema
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    is_valid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isValid')
    payload = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='payload')
    signature = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='signature')
    signer = sgqlc.types.Field('User', graphql_name='signer')
    state = sgqlc.types.Field(sgqlc.types.non_null(GitSignatureState), graphql_name='state')
    was_signed_by_git_hub = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='wasSignedByGitHub')


class SponsorsListing(sgqlc.types.Type, Node):
    __schema__ = github_schema
    full_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fullDescription')
    full_description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='fullDescriptionHTML')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    short_description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shortDescription')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    tiers = sgqlc.types.Field(SponsorsTierConnection, graphql_name='tiers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(SponsorsTierOrder, graphql_name='orderBy', default={'field': 'MONTHLY_PRICE_IN_CENTS', 'direction': 'ASC'})),
))
    )


class SponsorsTier(sgqlc.types.Type, Node):
    __schema__ = github_schema
    admin_info = sgqlc.types.Field(SponsorsTierAdminInfo, graphql_name='adminInfo')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    description_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='descriptionHTML')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    monthly_price_in_cents = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='monthlyPriceInCents')
    monthly_price_in_dollars = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='monthlyPriceInDollars')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    sponsors_listing = sgqlc.types.Field(sgqlc.types.non_null(SponsorsListing), graphql_name='sponsorsListing')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class Sponsorship(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    maintainer = sgqlc.types.Field(sgqlc.types.non_null('User'), graphql_name='maintainer')
    privacy_level = sgqlc.types.Field(sgqlc.types.non_null(SponsorshipPrivacy), graphql_name='privacyLevel')
    sponsor = sgqlc.types.Field('User', graphql_name='sponsor')
    tier = sgqlc.types.Field(SponsorsTier, graphql_name='tier')


class Status(sgqlc.types.Type, Node):
    __schema__ = github_schema
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    context = sgqlc.types.Field('StatusContext', graphql_name='context', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    contexts = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StatusContext'))), graphql_name='contexts')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    state = sgqlc.types.Field(sgqlc.types.non_null(StatusState), graphql_name='state')


class StatusContext(sgqlc.types.Type, Node):
    __schema__ = github_schema
    avatar_url = sgqlc.types.Field(URI, graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=40)),
))
    )
    commit = sgqlc.types.Field(Commit, graphql_name='commit')
    context = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='context')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    creator = sgqlc.types.Field(Actor, graphql_name='creator')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    state = sgqlc.types.Field(sgqlc.types.non_null(StatusState), graphql_name='state')
    target_url = sgqlc.types.Field(URI, graphql_name='targetUrl')


class SubscribedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    subscribable = sgqlc.types.Field(sgqlc.types.non_null(Subscribable), graphql_name='subscribable')


class Tag(sgqlc.types.Type, Node, GitObject):
    __schema__ = github_schema
    abbreviated_oid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='abbreviatedOid')
    commit_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitResourcePath')
    commit_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    message = sgqlc.types.Field(String, graphql_name='message')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')
    tagger = sgqlc.types.Field(GitActor, graphql_name='tagger')
    target = sgqlc.types.Field(sgqlc.types.non_null(GitObject), graphql_name='target')


class Team(sgqlc.types.Type, Node, Subscribable, MemberStatusable):
    __schema__ = github_schema
    ancestors = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='ancestors', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    avatar_url = sgqlc.types.Field(URI, graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=400)),
))
    )
    child_teams = sgqlc.types.Field(sgqlc.types.non_null(TeamConnection), graphql_name='childTeams', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(TeamOrder, graphql_name='orderBy', default=None)),
        ('user_logins', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='userLogins', default=None)),
        ('immediate_only', sgqlc.types.Arg(Boolean, graphql_name='immediateOnly', default=True)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    combined_slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='combinedSlug')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    description = sgqlc.types.Field(String, graphql_name='description')
    discussion = sgqlc.types.Field('TeamDiscussion', graphql_name='discussion', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    discussions = sgqlc.types.Field(sgqlc.types.non_null(TeamDiscussionConnection), graphql_name='discussions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('is_pinned', sgqlc.types.Arg(Boolean, graphql_name='isPinned', default=None)),
        ('order_by', sgqlc.types.Arg(TeamDiscussionOrder, graphql_name='orderBy', default=None)),
))
    )
    discussions_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='discussionsResourcePath')
    discussions_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='discussionsUrl')
    edit_team_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='editTeamResourcePath')
    edit_team_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='editTeamUrl')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    invitations = sgqlc.types.Field(OrganizationInvitationConnection, graphql_name='invitations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    member_statuses = sgqlc.types.Field(sgqlc.types.non_null(UserStatusConnection), graphql_name='memberStatuses', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(UserStatusOrder, graphql_name='orderBy', default={'field': 'UPDATED_AT', 'direction': 'DESC'})),
))
    )
    members = sgqlc.types.Field(sgqlc.types.non_null(TeamMemberConnection), graphql_name='members', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('membership', sgqlc.types.Arg(TeamMembershipType, graphql_name='membership', default='ALL')),
        ('role', sgqlc.types.Arg(TeamMemberRole, graphql_name='role', default=None)),
        ('order_by', sgqlc.types.Arg(TeamMemberOrder, graphql_name='orderBy', default=None)),
))
    )
    members_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='membersResourcePath')
    members_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='membersUrl')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    new_team_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='newTeamResourcePath')
    new_team_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='newTeamUrl')
    organization = sgqlc.types.Field(sgqlc.types.non_null(Organization), graphql_name='organization')
    parent_team = sgqlc.types.Field('Team', graphql_name='parentTeam')
    privacy = sgqlc.types.Field(sgqlc.types.non_null(TeamPrivacy), graphql_name='privacy')
    repositories = sgqlc.types.Field(sgqlc.types.non_null(TeamRepositoryConnection), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('query', sgqlc.types.Arg(String, graphql_name='query', default=None)),
        ('order_by', sgqlc.types.Arg(TeamRepositoryOrder, graphql_name='orderBy', default=None)),
))
    )
    repositories_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='repositoriesResourcePath')
    repositories_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='repositoriesUrl')
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    slug = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='slug')
    teams_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsResourcePath')
    teams_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='teamsUrl')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_administer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanAdminister')
    viewer_can_subscribe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSubscribe')
    viewer_subscription = sgqlc.types.Field(SubscriptionState, graphql_name='viewerSubscription')


class TeamAddMemberAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, TeamAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_ldap_mapped = sgqlc.types.Field(Boolean, graphql_name='isLdapMapped')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    team = sgqlc.types.Field(Team, graphql_name='team')
    team_name = sgqlc.types.Field(String, graphql_name='teamName')
    team_resource_path = sgqlc.types.Field(URI, graphql_name='teamResourcePath')
    team_url = sgqlc.types.Field(URI, graphql_name='teamUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class TeamAddRepositoryAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, RepositoryAuditEntryData, TeamAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_ldap_mapped = sgqlc.types.Field(Boolean, graphql_name='isLdapMapped')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field(Repository, graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    team = sgqlc.types.Field(Team, graphql_name='team')
    team_name = sgqlc.types.Field(String, graphql_name='teamName')
    team_resource_path = sgqlc.types.Field(URI, graphql_name='teamResourcePath')
    team_url = sgqlc.types.Field(URI, graphql_name='teamUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class TeamChangeParentTeamAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, TeamAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_ldap_mapped = sgqlc.types.Field(Boolean, graphql_name='isLdapMapped')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    parent_team = sgqlc.types.Field(Team, graphql_name='parentTeam')
    parent_team_name = sgqlc.types.Field(String, graphql_name='parentTeamName')
    parent_team_name_was = sgqlc.types.Field(String, graphql_name='parentTeamNameWas')
    parent_team_resource_path = sgqlc.types.Field(URI, graphql_name='parentTeamResourcePath')
    parent_team_url = sgqlc.types.Field(URI, graphql_name='parentTeamUrl')
    parent_team_was = sgqlc.types.Field(Team, graphql_name='parentTeamWas')
    parent_team_was_resource_path = sgqlc.types.Field(URI, graphql_name='parentTeamWasResourcePath')
    parent_team_was_url = sgqlc.types.Field(URI, graphql_name='parentTeamWasUrl')
    team = sgqlc.types.Field(Team, graphql_name='team')
    team_name = sgqlc.types.Field(String, graphql_name='teamName')
    team_resource_path = sgqlc.types.Field(URI, graphql_name='teamResourcePath')
    team_url = sgqlc.types.Field(URI, graphql_name='teamUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class TeamDiscussion(sgqlc.types.Type, Node, Comment, Deletable, Reactable, Subscribable, UniformResourceLocatable, Updatable, UpdatableComment):
    __schema__ = github_schema
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    body_version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyVersion')
    comments = sgqlc.types.Field(sgqlc.types.non_null(TeamDiscussionCommentConnection), graphql_name='comments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(TeamDiscussionCommentOrder, graphql_name='orderBy', default=None)),
        ('from_comment', sgqlc.types.Arg(Int, graphql_name='fromComment', default=None)),
))
    )
    comments_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commentsResourcePath')
    comments_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commentsUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    includes_created_edit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includesCreatedEdit')
    is_pinned = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPinned')
    is_private = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPrivate')
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ReactionGroup)), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(ReactionConnection), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    team = sgqlc.types.Field(sgqlc.types.non_null(Team), graphql_name='team')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    viewer_can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelete')
    viewer_can_pin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanPin')
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')
    viewer_can_subscribe = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanSubscribe')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')
    viewer_subscription = sgqlc.types.Field(SubscriptionState, graphql_name='viewerSubscription')


class TeamDiscussionComment(sgqlc.types.Type, Node, Comment, Deletable, Reactable, UniformResourceLocatable, Updatable, UpdatableComment):
    __schema__ = github_schema
    author = sgqlc.types.Field(Actor, graphql_name='author')
    author_association = sgqlc.types.Field(sgqlc.types.non_null(CommentAuthorAssociation), graphql_name='authorAssociation')
    body = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='body')
    body_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bodyHTML')
    body_text = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyText')
    body_version = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bodyVersion')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    created_via_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='createdViaEmail')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    discussion = sgqlc.types.Field(sgqlc.types.non_null(TeamDiscussion), graphql_name='discussion')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    includes_created_edit = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='includesCreatedEdit')
    last_edited_at = sgqlc.types.Field(DateTime, graphql_name='lastEditedAt')
    number = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='number')
    published_at = sgqlc.types.Field(DateTime, graphql_name='publishedAt')
    reaction_groups = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(ReactionGroup)), graphql_name='reactionGroups')
    reactions = sgqlc.types.Field(sgqlc.types.non_null(ReactionConnection), graphql_name='reactions', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('content', sgqlc.types.Arg(ReactionContent, graphql_name='content', default=None)),
        ('order_by', sgqlc.types.Arg(ReactionOrder, graphql_name='orderBy', default=None)),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    user_content_edits = sgqlc.types.Field(UserContentEditConnection, graphql_name='userContentEdits', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    viewer_can_delete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanDelete')
    viewer_can_react = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanReact')
    viewer_can_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanUpdate')
    viewer_cannot_update_reasons = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(CommentCannotUpdateReason))), graphql_name='viewerCannotUpdateReasons')
    viewer_did_author = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerDidAuthor')


class TeamRemoveMemberAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, TeamAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_ldap_mapped = sgqlc.types.Field(Boolean, graphql_name='isLdapMapped')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    team = sgqlc.types.Field(Team, graphql_name='team')
    team_name = sgqlc.types.Field(String, graphql_name='teamName')
    team_resource_path = sgqlc.types.Field(URI, graphql_name='teamResourcePath')
    team_url = sgqlc.types.Field(URI, graphql_name='teamUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class TeamRemoveRepositoryAuditEntry(sgqlc.types.Type, Node, AuditEntry, OrganizationAuditEntryData, RepositoryAuditEntryData, TeamAuditEntryData):
    __schema__ = github_schema
    action = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='action')
    actor = sgqlc.types.Field('AuditEntryActor', graphql_name='actor')
    actor_ip = sgqlc.types.Field(String, graphql_name='actorIp')
    actor_location = sgqlc.types.Field(ActorLocation, graphql_name='actorLocation')
    actor_login = sgqlc.types.Field(String, graphql_name='actorLogin')
    actor_resource_path = sgqlc.types.Field(URI, graphql_name='actorResourcePath')
    actor_url = sgqlc.types.Field(URI, graphql_name='actorUrl')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(PreciseDateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_ldap_mapped = sgqlc.types.Field(Boolean, graphql_name='isLdapMapped')
    operation_type = sgqlc.types.Field(OperationType, graphql_name='operationType')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    organization_name = sgqlc.types.Field(String, graphql_name='organizationName')
    organization_resource_path = sgqlc.types.Field(URI, graphql_name='organizationResourcePath')
    organization_url = sgqlc.types.Field(URI, graphql_name='organizationUrl')
    repository = sgqlc.types.Field(Repository, graphql_name='repository')
    repository_name = sgqlc.types.Field(String, graphql_name='repositoryName')
    repository_resource_path = sgqlc.types.Field(URI, graphql_name='repositoryResourcePath')
    repository_url = sgqlc.types.Field(URI, graphql_name='repositoryUrl')
    team = sgqlc.types.Field(Team, graphql_name='team')
    team_name = sgqlc.types.Field(String, graphql_name='teamName')
    team_resource_path = sgqlc.types.Field(URI, graphql_name='teamResourcePath')
    team_url = sgqlc.types.Field(URI, graphql_name='teamUrl')
    user = sgqlc.types.Field('User', graphql_name='user')
    user_login = sgqlc.types.Field(String, graphql_name='userLogin')
    user_resource_path = sgqlc.types.Field(URI, graphql_name='userResourcePath')
    user_url = sgqlc.types.Field(URI, graphql_name='userUrl')


class Topic(sgqlc.types.Type, Node, Starrable):
    __schema__ = github_schema
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    related_topics = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Topic'))), graphql_name='relatedTopics', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=3)),
))
    )
    stargazers = sgqlc.types.Field(sgqlc.types.non_null(StargazerConnection), graphql_name='stargazers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(StarOrder, graphql_name='orderBy', default=None)),
))
    )
    viewer_has_starred = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerHasStarred')


class TransferredEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    from_repository = sgqlc.types.Field(Repository, graphql_name='fromRepository')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')


class Tree(sgqlc.types.Type, Node, GitObject):
    __schema__ = github_schema
    abbreviated_oid = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='abbreviatedOid')
    commit_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitResourcePath')
    commit_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='commitUrl')
    entries = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(TreeEntry)), graphql_name='entries')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    oid = sgqlc.types.Field(sgqlc.types.non_null(GitObjectID), graphql_name='oid')
    repository = sgqlc.types.Field(sgqlc.types.non_null(Repository), graphql_name='repository')


class UnassignedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    assignable = sgqlc.types.Field(sgqlc.types.non_null(Assignable), graphql_name='assignable')
    assignee = sgqlc.types.Field('Assignee', graphql_name='assignee')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')


class UnknownSignature(sgqlc.types.Type, GitSignature):
    __schema__ = github_schema
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    is_valid = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isValid')
    payload = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='payload')
    signature = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='signature')
    signer = sgqlc.types.Field('User', graphql_name='signer')
    state = sgqlc.types.Field(sgqlc.types.non_null(GitSignatureState), graphql_name='state')
    was_signed_by_git_hub = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='wasSignedByGitHub')


class UnlabeledEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    label = sgqlc.types.Field(sgqlc.types.non_null(Label), graphql_name='label')
    labelable = sgqlc.types.Field(sgqlc.types.non_null(Labelable), graphql_name='labelable')


class UnlockedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    lockable = sgqlc.types.Field(sgqlc.types.non_null(Lockable), graphql_name='lockable')


class UnpinnedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    issue = sgqlc.types.Field(sgqlc.types.non_null(Issue), graphql_name='issue')


class UnsubscribedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    subscribable = sgqlc.types.Field(sgqlc.types.non_null(Subscribable), graphql_name='subscribable')


class User(sgqlc.types.Type, Node, Actor, RegistryPackageOwner, RegistryPackageSearch, ProjectOwner, RepositoryOwner, UniformResourceLocatable, ProfileOwner, Sponsorable):
    __schema__ = github_schema
    any_pinnable_items = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='anyPinnableItems', args=sgqlc.types.ArgDict((
        ('type', sgqlc.types.Arg(PinnableItemType, graphql_name='type', default=None)),
))
    )
    avatar_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='avatarUrl', args=sgqlc.types.ArgDict((
        ('size', sgqlc.types.Arg(Int, graphql_name='size', default=None)),
))
    )
    bio = sgqlc.types.Field(String, graphql_name='bio')
    bio_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='bioHTML')
    commit_comments = sgqlc.types.Field(sgqlc.types.non_null(CommitCommentConnection), graphql_name='commitComments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    company = sgqlc.types.Field(String, graphql_name='company')
    company_html = sgqlc.types.Field(sgqlc.types.non_null(HTML), graphql_name='companyHTML')
    contributions_collection = sgqlc.types.Field(sgqlc.types.non_null(ContributionsCollection), graphql_name='contributionsCollection', args=sgqlc.types.ArgDict((
        ('organization_id', sgqlc.types.Arg(ID, graphql_name='organizationID', default=None)),
        ('from_', sgqlc.types.Arg(DateTime, graphql_name='from', default=None)),
        ('to', sgqlc.types.Arg(DateTime, graphql_name='to', default=None)),
))
    )
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    database_id = sgqlc.types.Field(Int, graphql_name='databaseId')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    followers = sgqlc.types.Field(sgqlc.types.non_null(FollowerConnection), graphql_name='followers', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    following = sgqlc.types.Field(sgqlc.types.non_null(FollowingConnection), graphql_name='following', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    gist = sgqlc.types.Field(Gist, graphql_name='gist', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    gist_comments = sgqlc.types.Field(sgqlc.types.non_null(GistCommentConnection), graphql_name='gistComments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    gists = sgqlc.types.Field(sgqlc.types.non_null(GistConnection), graphql_name='gists', args=sgqlc.types.ArgDict((
        ('privacy', sgqlc.types.Arg(GistPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(GistOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    hovercard = sgqlc.types.Field(sgqlc.types.non_null(Hovercard), graphql_name='hovercard', args=sgqlc.types.ArgDict((
        ('primary_subject_id', sgqlc.types.Arg(ID, graphql_name='primarySubjectId', default=None)),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    is_bounty_hunter = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isBountyHunter')
    is_campus_expert = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isCampusExpert')
    is_developer_program_member = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDeveloperProgramMember')
    is_employee = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEmployee')
    is_hireable = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isHireable')
    is_site_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isSiteAdmin')
    is_viewer = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isViewer')
    issue_comments = sgqlc.types.Field(sgqlc.types.non_null(IssueCommentConnection), graphql_name='issueComments', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    issues = sgqlc.types.Field(sgqlc.types.non_null(IssueConnection), graphql_name='issues', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(IssueState)), graphql_name='states', default=None)),
        ('filter_by', sgqlc.types.Arg(IssueFilters, graphql_name='filterBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    item_showcase = sgqlc.types.Field(sgqlc.types.non_null(ProfileItemShowcase), graphql_name='itemShowcase')
    location = sgqlc.types.Field(String, graphql_name='location')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    name = sgqlc.types.Field(String, graphql_name='name')
    organization = sgqlc.types.Field(Organization, graphql_name='organization', args=sgqlc.types.ArgDict((
        ('login', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='login', default=None)),
))
    )
    organizations = sgqlc.types.Field(sgqlc.types.non_null(OrganizationConnection), graphql_name='organizations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pinnable_items = sgqlc.types.Field(sgqlc.types.non_null(PinnableItemConnection), graphql_name='pinnableItems', args=sgqlc.types.ArgDict((
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PinnableItemType)), graphql_name='types', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pinned_items = sgqlc.types.Field(sgqlc.types.non_null(PinnableItemConnection), graphql_name='pinnedItems', args=sgqlc.types.ArgDict((
        ('types', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PinnableItemType)), graphql_name='types', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pinned_items_remaining = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pinnedItemsRemaining')
    project = sgqlc.types.Field(Project, graphql_name='project', args=sgqlc.types.ArgDict((
        ('number', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='number', default=None)),
))
    )
    projects = sgqlc.types.Field(sgqlc.types.non_null(ProjectConnection), graphql_name='projects', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(ProjectOrder, graphql_name='orderBy', default=None)),
        ('search', sgqlc.types.Arg(String, graphql_name='search', default=None)),
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProjectState)), graphql_name='states', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    projects_resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsResourcePath')
    projects_url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='projectsUrl')
    public_keys = sgqlc.types.Field(sgqlc.types.non_null(PublicKeyConnection), graphql_name='publicKeys', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    pull_requests = sgqlc.types.Field(sgqlc.types.non_null(PullRequestConnection), graphql_name='pullRequests', args=sgqlc.types.ArgDict((
        ('states', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PullRequestState)), graphql_name='states', default=None)),
        ('labels', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(String)), graphql_name='labels', default=None)),
        ('head_ref_name', sgqlc.types.Arg(String, graphql_name='headRefName', default=None)),
        ('base_ref_name', sgqlc.types.Arg(String, graphql_name='baseRefName', default=None)),
        ('order_by', sgqlc.types.Arg(IssueOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    repositories = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='repositories', args=sgqlc.types.ArgDict((
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=['OWNER', 'COLLABORATOR'])),
        ('owner_affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='ownerAffiliations', default=['OWNER', 'COLLABORATOR'])),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('is_fork', sgqlc.types.Arg(Boolean, graphql_name='isFork', default=None)),
))
    )
    repositories_contributed_to = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='repositoriesContributedTo', args=sgqlc.types.ArgDict((
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
        ('include_user_repositories', sgqlc.types.Arg(Boolean, graphql_name='includeUserRepositories', default=None)),
        ('contribution_types', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryContributionType), graphql_name='contributionTypes', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    repository = sgqlc.types.Field(Repository, graphql_name='repository', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    resource_path = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='resourcePath')
    saved_replies = sgqlc.types.Field(SavedReplyConnection, graphql_name='savedReplies', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(SavedReplyOrder, graphql_name='orderBy', default={'field': 'UPDATED_AT', 'direction': 'DESC'})),
))
    )
    sponsors_listing = sgqlc.types.Field(SponsorsListing, graphql_name='sponsorsListing')
    sponsorships_as_maintainer = sgqlc.types.Field(sgqlc.types.non_null(SponsorshipConnection), graphql_name='sponsorshipsAsMaintainer', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('include_private', sgqlc.types.Arg(Boolean, graphql_name='includePrivate', default=False)),
        ('order_by', sgqlc.types.Arg(SponsorshipOrder, graphql_name='orderBy', default=None)),
))
    )
    sponsorships_as_sponsor = sgqlc.types.Field(sgqlc.types.non_null(SponsorshipConnection), graphql_name='sponsorshipsAsSponsor', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(SponsorshipOrder, graphql_name='orderBy', default=None)),
))
    )
    starred_repositories = sgqlc.types.Field(sgqlc.types.non_null(StarredRepositoryConnection), graphql_name='starredRepositories', args=sgqlc.types.ArgDict((
        ('owned_by_viewer', sgqlc.types.Arg(Boolean, graphql_name='ownedByViewer', default=None)),
        ('order_by', sgqlc.types.Arg(StarOrder, graphql_name='orderBy', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    status = sgqlc.types.Field('UserStatus', graphql_name='status')
    top_repositories = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='topRepositories', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.non_null(RepositoryOrder), graphql_name='orderBy', default=None)),
        ('since', sgqlc.types.Arg(DateTime, graphql_name='since', default=None)),
))
    )
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    url = sgqlc.types.Field(sgqlc.types.non_null(URI), graphql_name='url')
    viewer_can_change_pinned_items = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanChangePinnedItems')
    viewer_can_create_projects = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanCreateProjects')
    viewer_can_follow = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerCanFollow')
    viewer_is_following = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='viewerIsFollowing')
    watching = sgqlc.types.Field(sgqlc.types.non_null(RepositoryConnection), graphql_name='watching', args=sgqlc.types.ArgDict((
        ('privacy', sgqlc.types.Arg(RepositoryPrivacy, graphql_name='privacy', default=None)),
        ('order_by', sgqlc.types.Arg(RepositoryOrder, graphql_name='orderBy', default=None)),
        ('affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='affiliations', default=['OWNER', 'COLLABORATOR', 'ORGANIZATION_MEMBER'])),
        ('owner_affiliations', sgqlc.types.Arg(sgqlc.types.list_of(RepositoryAffiliation), graphql_name='ownerAffiliations', default=['OWNER', 'COLLABORATOR'])),
        ('is_locked', sgqlc.types.Arg(Boolean, graphql_name='isLocked', default=None)),
        ('after', sgqlc.types.Arg(String, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(String, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
))
    )
    website_url = sgqlc.types.Field(URI, graphql_name='websiteUrl')


class UserBlockedEvent(sgqlc.types.Type, Node):
    __schema__ = github_schema
    actor = sgqlc.types.Field(Actor, graphql_name='actor')
    block_duration = sgqlc.types.Field(sgqlc.types.non_null(UserBlockDuration), graphql_name='blockDuration')
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    subject = sgqlc.types.Field(User, graphql_name='subject')


class UserContentEdit(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    deleted_at = sgqlc.types.Field(DateTime, graphql_name='deletedAt')
    deleted_by = sgqlc.types.Field(Actor, graphql_name='deletedBy')
    diff = sgqlc.types.Field(String, graphql_name='diff')
    edited_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='editedAt')
    editor = sgqlc.types.Field(Actor, graphql_name='editor')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')


class UserStatus(sgqlc.types.Type, Node):
    __schema__ = github_schema
    created_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='createdAt')
    emoji = sgqlc.types.Field(String, graphql_name='emoji')
    emoji_html = sgqlc.types.Field(HTML, graphql_name='emojiHTML')
    expires_at = sgqlc.types.Field(DateTime, graphql_name='expiresAt')
    id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='id')
    indicates_limited_availability = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='indicatesLimitedAvailability')
    message = sgqlc.types.Field(String, graphql_name='message')
    organization = sgqlc.types.Field(Organization, graphql_name='organization')
    updated_at = sgqlc.types.Field(sgqlc.types.non_null(DateTime), graphql_name='updatedAt')
    user = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='user')


class ViewerHovercardContext(sgqlc.types.Type, HovercardContext):
    __schema__ = github_schema
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')
    octicon = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='octicon')
    viewer = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='viewer')



########################################################################
# Unions
########################################################################
class Assignee(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Bot, Mannequin, Organization, User)


class AuditEntryActor(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Bot, Organization, User)


class Closer(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Commit, PullRequest)


class CollectionItemContent(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Repository, Organization, User)


class CreatedIssueOrRestrictedContribution(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (CreatedIssueContribution, RestrictedContribution)


class CreatedPullRequestOrRestrictedContribution(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (CreatedPullRequestContribution, RestrictedContribution)


class CreatedRepositoryOrRestrictedContribution(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (CreatedRepositoryContribution, RestrictedContribution)


class EnterpriseMember(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (User, EnterpriseUserAccount)


class IssueOrPullRequest(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Issue, PullRequest)


class IssueTimelineItem(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Commit, IssueComment, CrossReferencedEvent, ClosedEvent, ReopenedEvent, SubscribedEvent, UnsubscribedEvent, ReferencedEvent, AssignedEvent, UnassignedEvent, LabeledEvent, UnlabeledEvent, UserBlockedEvent, MilestonedEvent, DemilestonedEvent, RenamedTitleEvent, LockedEvent, UnlockedEvent, TransferredEvent)


class IssueTimelineItems(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (IssueComment, CrossReferencedEvent, AddedToProjectEvent, AssignedEvent, ClosedEvent, CommentDeletedEvent, ConvertedNoteToIssueEvent, DemilestonedEvent, LabeledEvent, LockedEvent, MarkedAsDuplicateEvent, MentionedEvent, MilestonedEvent, MovedColumnsInProjectEvent, PinnedEvent, ReferencedEvent, RemovedFromProjectEvent, RenamedTitleEvent, ReopenedEvent, SubscribedEvent, TransferredEvent, UnassignedEvent, UnlabeledEvent, UnlockedEvent, UserBlockedEvent, UnpinnedEvent, UnsubscribedEvent)


class MilestoneItem(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Issue, PullRequest)


class OrgRestoreMemberAuditEntryMembership(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (OrgRestoreMemberMembershipOrganizationAuditEntryData, OrgRestoreMemberMembershipRepositoryAuditEntryData, OrgRestoreMemberMembershipTeamAuditEntryData)


class OrganizationAuditEntry(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (MembersCanDeleteReposClearAuditEntry, MembersCanDeleteReposDisableAuditEntry, MembersCanDeleteReposEnableAuditEntry, OauthApplicationCreateAuditEntry, OrgAddBillingManagerAuditEntry, OrgAddMemberAuditEntry, OrgBlockUserAuditEntry, OrgConfigDisableCollaboratorsOnlyAuditEntry, OrgConfigEnableCollaboratorsOnlyAuditEntry, OrgCreateAuditEntry, OrgDisableOauthAppRestrictionsAuditEntry, OrgDisableSamlAuditEntry, OrgDisableTwoFactorRequirementAuditEntry, OrgEnableOauthAppRestrictionsAuditEntry, OrgEnableSamlAuditEntry, OrgEnableTwoFactorRequirementAuditEntry, OrgInviteMemberAuditEntry, OrgInviteToBusinessAuditEntry, OrgOauthAppAccessApprovedAuditEntry, OrgOauthAppAccessDeniedAuditEntry, OrgOauthAppAccessRequestedAuditEntry, OrgRemoveBillingManagerAuditEntry, OrgRemoveMemberAuditEntry, OrgRemoveOutsideCollaboratorAuditEntry, OrgRestoreMemberAuditEntry, OrgUnblockUserAuditEntry, OrgUpdateDefaultRepositoryPermissionAuditEntry, OrgUpdateMemberAuditEntry, OrgUpdateMemberRepositoryCreationPermissionAuditEntry, OrgUpdateMemberRepositoryInvitationPermissionAuditEntry, PrivateRepositoryForkingDisableAuditEntry, PrivateRepositoryForkingEnableAuditEntry, RepoAccessAuditEntry, RepoAddMemberAuditEntry, RepoAddTopicAuditEntry, RepoArchivedAuditEntry, RepoChangeMergeSettingAuditEntry, RepoConfigDisableAnonymousGitAccessAuditEntry, RepoConfigDisableCollaboratorsOnlyAuditEntry, RepoConfigDisableContributorsOnlyAuditEntry, RepoConfigDisableSockpuppetDisallowedAuditEntry, RepoConfigEnableAnonymousGitAccessAuditEntry, RepoConfigEnableCollaboratorsOnlyAuditEntry, RepoConfigEnableContributorsOnlyAuditEntry, RepoConfigEnableSockpuppetDisallowedAuditEntry, RepoConfigLockAnonymousGitAccessAuditEntry, RepoConfigUnlockAnonymousGitAccessAuditEntry, RepoCreateAuditEntry, RepoDestroyAuditEntry, RepoRemoveMemberAuditEntry, RepoRemoveTopicAuditEntry, RepositoryVisibilityChangeDisableAuditEntry, RepositoryVisibilityChangeEnableAuditEntry, TeamAddMemberAuditEntry, TeamAddRepositoryAuditEntry, TeamChangeParentTeamAuditEntry, TeamRemoveMemberAuditEntry, TeamRemoveRepositoryAuditEntry)


class PermissionGranter(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Organization, Repository, Team)


class PinnableItem(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Gist, Repository)


class ProjectCardItem(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Issue, PullRequest)


class PullRequestTimelineItem(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Commit, CommitCommentThread, PullRequestReview, PullRequestReviewThread, PullRequestReviewComment, IssueComment, ClosedEvent, ReopenedEvent, SubscribedEvent, UnsubscribedEvent, MergedEvent, ReferencedEvent, CrossReferencedEvent, AssignedEvent, UnassignedEvent, LabeledEvent, UnlabeledEvent, MilestonedEvent, DemilestonedEvent, RenamedTitleEvent, LockedEvent, UnlockedEvent, DeployedEvent, DeploymentEnvironmentChangedEvent, HeadRefDeletedEvent, HeadRefRestoredEvent, HeadRefForcePushedEvent, BaseRefForcePushedEvent, ReviewRequestedEvent, ReviewRequestRemovedEvent, ReviewDismissedEvent, UserBlockedEvent)


class PullRequestTimelineItems(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (PullRequestCommit, PullRequestCommitCommentThread, PullRequestReview, PullRequestReviewThread, PullRequestRevisionMarker, BaseRefChangedEvent, BaseRefForcePushedEvent, DeployedEvent, DeploymentEnvironmentChangedEvent, HeadRefDeletedEvent, HeadRefForcePushedEvent, HeadRefRestoredEvent, MergedEvent, ReviewDismissedEvent, ReviewRequestedEvent, ReviewRequestRemovedEvent, ReadyForReviewEvent, IssueComment, CrossReferencedEvent, AddedToProjectEvent, AssignedEvent, ClosedEvent, CommentDeletedEvent, ConvertedNoteToIssueEvent, DemilestonedEvent, LabeledEvent, LockedEvent, MarkedAsDuplicateEvent, MentionedEvent, MilestonedEvent, MovedColumnsInProjectEvent, PinnedEvent, ReferencedEvent, RemovedFromProjectEvent, RenamedTitleEvent, ReopenedEvent, SubscribedEvent, TransferredEvent, UnassignedEvent, UnlabeledEvent, UnlockedEvent, UserBlockedEvent, UnpinnedEvent, UnsubscribedEvent)


class PushAllowanceActor(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (User, Team, App)


class ReferencedSubject(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Issue, PullRequest)


class RenamedTitleSubject(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Issue, PullRequest)


class RequestedReviewer(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (User, Team, Mannequin)


class ReviewDismissalAllowanceActor(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (User, Team)


class SearchResultItem(sgqlc.types.Union):
    __schema__ = github_schema
    __types__ = (Issue, PullRequest, Repository, User, Organization, MarketplaceListing, App)



########################################################################
# Schema Entry Points
########################################################################
github_schema.query_type = Query
github_schema.mutation_type = Mutation
github_schema.subscription_type = None

